example = [
'#.#####################',
'#.......#########...###',
'#######.#########.#.###',
'###.....#.>.>.###.#.###',
'###v#####.#v#.###.#.###',
'###.>...#.#.#.....#...#',
'###v###.#.#.#########.#',
'###...#.#.#.......#...#',
'#####.#.#.#######.#.###',
'#.....#.#.#.......#...#',
'#.#####.#.#.#########v#',
'#.#...#...#...###...>.#',
'#.#.#v#######v###.###v#',
'#...#.>.#...>.>.#.###.#',
'#####v#.#.###v#.#.###.#',
'#.....#...#...#.#.#...#',
'#.#########.###.#.#.###',
'#...###...#...#...#.###',
'###.###.#.###v#####v###',
'#...#...#.#.>.>.#.>.###',
'#.###.###.#.###.#.#v###',
'#.....###...###...#...#',
'#####################.#',
]

with open("2023\Day22\day22_input.txt", "r") as f:
    map = [line.strip() for line in f]

use_real_data = False
if not use_real_data:
    map = example


for i,row in enumerate(map):
    map[i] = list(map[i])


start_cord = (0,1)

slopes = ["<",">","^","v"]

def slopeCord(map,x,y):
    match map[x][y]:
        case ">":
            return (x,y+1)
        case "<":
            return (x,y-1)
        case "v":
            return (x+1,y)
        case "^":
            return (x-1,y)

def neighborCords(map,x,y):
    neighbors = [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]
    uphills = ["v","^","<",">"]
    valid_step = []
    for neigh,opposite in zip(neighbors,uphills):
        if map[neigh[0]][neigh[1]] not in ["#","O"] and neigh[0]<len(map)-1 and neigh[1]<len(map[0])-1:
            if map[neigh[0]][neigh[1]] != opposite:
                valid_step.append(neigh)
    return valid_step

steps = [[map,start_cord,0]]
s = []
#while steps != []:
for x in range(75):
    end = False
    curr_map = steps[0][0]
    curr_cord = steps[0][1]
    steps_taken = steps[0][2]
    tile = curr_map[curr_cord[0]][curr_cord[1]]
    #print(tile)
    if tile == ".":
        curr_map[curr_cord[0]][curr_cord[1]] = "O"

    elif tile in slopes:
        '''for x in curr_map:
            print(''.join(x))
        print(curr_cord[0],curr_cord[1])'''
        new_cord = slopeCord(curr_map,curr_cord[0],curr_cord[1])
        curr_map[curr_cord[0]][curr_cord[1]] = "O"
        curr_map[new_cord[0]][new_cord[1]] = "O"
        curr_cord = new_cord
        steps_taken += 1

    neighbors = neighborCords(curr_map,curr_cord[0],curr_cord[1])
    if neighbors != []:
        for neigh in neighbors:
            steps.insert(1,[curr_map,neigh,steps_taken+1])
    
    else:
        s.append(steps_taken)


    steps = steps[1::]
print(s)

for x in curr_map:
    print("".join(x))
