example = [
".....",
".S-7.",
".|.|.",
".L-J.",
"....."
]

with open("Day10\day10_input.txt", "r") as f:
    map = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    map = example


for i in range(len(map)):
    map[i] = "." + map[i] + "."
map = ["." * len(map[0])] + map + ["." * len(map[0])]

#creating a dict with 0s and 1s to track the sides with connection 
#0 - can't connect      1 - can connect
#[up,down,right,left]
types = {
    "|": [1,1,0,0],
    "-": [0,0,1,1],
    "L": [1,0,1,0],
    "J": [1,0,0,1],
    "7": [0,1,0,1],
    "F": [0,1,1,0],
    "S": [1,1,1,1],
    ".": [0,0,0,0],
    "#": [0,0,0,0]   # Hashtag is an extras just for visualization
}

#finding the starting point
for row in map:
    if "S" in row:
        s = (map.index(row), row.index("S"))

#checks the surrounding of a pipe and returns the cordinates of those that it can be connected
def neighborChacker(map,cord):
    x = cord[0]
    y = cord[1]
    can_move = []
    if types[map[x][y]][0] == types[map[x-1][y]][1] == 1: #up
        can_move.append((x-1, y))
    if types[map[x][y]][1] == types[map[x+1][y]][0] == 1: #down
        can_move.append((x+1,y))
    if types[map[x][y]][2] == types[map[x][y+1]][3] == 1: #right
        can_move.append((x, y+1))
    if types[map[x][y]][3] == types[map[x][y-1]][2] == 1: #left
        can_move.append((x, y-1))

    return can_move

#replaces the already 'visited' pipes so that the neighborChecker can't retun it again
def replaceWithHash(map,cord):
    split_row = [char for char in map[cord[0]]]
    split_row[cord[1]] = "#"
    return "".join(split_row)

#using both functions on the startingpoint
hashed_map = [x for x in map]

cords = neighborChacker(hashed_map,s)
hashed_map[s[0]] = replaceWithHash(hashed_map,s)



farthest = 0
while cords != []:
    new_cords = []
    for cord in cords:
        new_cords += neighborChacker(hashed_map,cord)
        hashed_map[cord[0]] = replaceWithHash(hashed_map,cord)
    farthest += 1
    cords = new_cords


print(f"Part 1 answer: {farthest}")

#creating a new map that shows the main loop, anything else is replaced with 0s
loop_map = []
for x,row in enumerate(hashed_map):
    loop_line = ""
    for y,char in enumerate(row):
        if char == "#":
            loop_line += map[x][y]
        else:
            loop_line += "0"
    loop_map.append(loop_line)


#Replacein 0s with X if there are any non-0 characters in each directions
def maybeEnclosed(map,cord): #(43,32)
    gate = [0,0,0,0]
    row_len = len(map[0])
    row_num = len(map)

    for x in range(cord[0],0,-1):
        #print(cord[0]+x)
        if map[x][cord[1]] != "0":
            gate[0] = 1
            break

    for x in range(cord[0],row_num):
        if map[x][cord[1]] != "0":
            gate[1] = 1
            break
    
    for y in range(cord[1],0,-1):
        if map[cord[0]][y] != "0":
            gate[2] = 1
            break

    for y in range(cord[1],row_len):
        if map[cord[0]][y] != "0":
            gate[3] = 1
            break

    if gate == [1,1,1,1]:
        return "X"
    else:
        return "0"
    

for x,row in enumerate(loop_map[1:-1]):
    row = list(row)
    for y,char in enumerate(row[1:-1]):
        if char == "0":
            #print(x,y)
            row[y+1] = maybeEnclosed(loop_map, (x+1,y+1))
    loop_map[x+1] = "".join(row)

#if not all sides of a character are, then it's a direct border of the loop
#border remains 0, anything else is transformed int dots
def border(map,cord):
    x = cord[0]
    y = cord[1]
    c = ["0", "."]
    if x == 0 or y == 0 or x == len(map)-1 or y == len(map[0])-1:
        return "."
    elif map[x+1][y] in c and map[x-1][y] in c and map[x][y+1] in c and map[x][y-1] in c:
        return "."
    else:
        return "0"




for x,row in enumerate(loop_map):
    row = list(row)
    for y,char in enumerate(row):
        if char == "0":
                row[y] = border(loop_map, (x,y))
    loop_map[x] = "".join(row)


#looping through another time to replace all X that has a "0" next to them
    
"""for x,row in enumerate(loop_map):
    row = list(row)
    for y,char in enumerate(row):
        if char == "X":
            if loop_map[x+1][y] == "0":
                loop_map[x+1] = list(loop_map[x+1])
                loop_map[x+1][y] = "0"
                loop_map[x+1] = "".join(loop_map[x+1])
            if loop_map[x-1][y] == "0":
                loop_map[x-1] = list(loop_map[x-1])
                loop_map[x-1][y] = "0"
                loop_map[x-1] = "".join(loop_map[x-1])
            if loop_map[x][y+1] == "0":
                loop_map[x] = list(loop_map[x])
                loop_map[x][y+1] = "0"
                loop_map[x] = "".join(loop_map[x])
            if loop_map[x][y-1] == "0":
                loop_map[x] = list(loop_map[x])
                loop_map[x][y-1] = "0"
                loop_map[x] = "".join(loop_map[x])"""


types["X"] = [1,1,1,1]
types["0"] = [-1,-1,-1,-1]



#finding all the Xs, they are starting points
start = []
for row in loop_map:
    if "X" in row:
        start.append((loop_map.index(row), row.index("X")))


def borderChecker(map,cord):
    x = cord[0]
    y = cord[1]
    zero = []
    if types[map[x][y]][0] == 1 and types[map[x-1][y]][1] == -1: #up
        zero.append((x-1, y))
    if types[map[x][y]][1] == 1 and types[map[x+1][y]][0] == -1: #down
        zero.append((x+1,y))
    if types[map[x][y]][2] == 1 and types[map[x][y+1]][3] == -1: #right
        zero.append((x, y+1))
    if types[map[x][y]][3] == 1 and types[map[x][y-1]][2] == -1: #left
        zero.append((x, y-1))

    return zero


for x_cord in start:
    temp_map = [x for x in loop_map]
    cords = neighborChacker(temp_map,x_cord)
    temp_map[x_cord[0]] = replaceWithHash(temp_map,x_cord)
    zeros = []
    while cords != []:
        
        new_cords = []
        for cord in cords:
            new_cords += neighborChacker(temp_map,cord)
            zeros += borderChecker(temp_map,cord)

            temp_map[cord[0]] = replaceWithHash(temp_map,cord)
        cords = new_cords
    if zeros != []:
        loop_map[x_cord[0]] = list(loop_map[x_cord[0]])
        loop_map[x_cord[0]][x_cord[1]] = "0"
        loop_map[x_cord[0]] = "".join(loop_map[x_cord[0]])
    
                

"""for x_cord in start:
    temp_map = loop_map
    while new_cords != []:
        new_cords = [x_cord]
        zero_cords = []
        for cord in cords:
            new_cords += neighborChacker(temp_map,cord)
            zero_cords += borderChecker(temp_map,cord)
            if zero_cords != []:
                loop_map[x_cord[0]] = list(loop_map[x_cord[0]])
                loop_map[x_cord[0]][x_cord[1]] = "W"
                loop_map[x_cord[0]] = "".join(loop_map[x_cord[0]])
                break
            temp_map[cord[0]] = replaceWithHash(temp_map,cord)
        cords = new_cords
    start.remove(x_cord)"""


for line in loop_map:
    print(line)

p = 0
for l in loop_map:
    p += l.count("X")
print(p)






#710 too high