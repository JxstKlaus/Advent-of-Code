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
print(map)
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
def neighborChacker(cord):
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
cords = neighborChacker(s)
map[s[0]] = replaceWithHash(map,s)
print(cords)


farthest = 0
while cords != []:
    new_cords = []
    for cord in cords:
        
        #print(map[cord[0]][cord[1]])
        #print(cord)
        new_cords += neighborChacker(cord)
        map[cord[0]] = replaceWithHash(map,cord)
    farthest += 1
    cords = new_cords
    #print(cords)

print(f"Part 1 answer: {farthest}")
