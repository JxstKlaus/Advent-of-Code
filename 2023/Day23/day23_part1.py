import copy
example = [
"#.#####################",
"#.......#########...###",
"#######.#########.#.###",
"###.....#.>.>.###.#.###",
"###v#####.#v#.###.#.###",
"###.>...#.#.#.....#...#",
"###v###.#.#.#########.#",
"###...#.#.#.......#...#",
"#####.#.#.#######.#.###",
"#.....#.#.#.......#...#",
"#.#####.#.#.#########v#",
"#.#...#...#...###...>.#",
"#.#.#v#######v###.###v#",
"#...#.>.#...>.>.#.###.#",
"#####v#.#.###v#.#.###.#",
"#.....#...#...#.#.#...#",
"#.#########.###.#.#.###",
"#...###...#...#...#.###",
"###.###.#.###v#####v###",
"#...#...#.#.>.>.#.>.###",
"#.###.###.#.###.#.#v###",
"#.....###...###...#...#",
"#####################.#"
]

with open("day23_input.txt", "r") as f:
    data = [x.strip() for x in f]

use_real_data = True
if not use_real_data:
    data = example

for i,line in enumerate(data):
    data[i] = list(line)

def getValidNeighbors(map,x,y):
    valid = []
    neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    opposite = ["^","v","<", ">"]
    for neigh, opp in zip(neighbors,opposite):
        if map[neigh[0]][neigh[1]] not in ["#","O", opp] and neigh[0]<len(map)-1 and neigh[1]<len(map[0])-1:
            valid.append(neigh)
    return valid

def slope(map,x,y):
    match map[x][y]:
        case "^":
            return (x-1,y)
        case "v":
            return (x+1,y)
        case "<":
            return (x,y-1)
        case ">":
            return (x,y+1)

steps = [[data,(0,1),0]]


longest = 0
while steps != []:
#for _ in range(36):
    hike_map = steps[0][0]
    curr_cord = steps[0][1]
    steps_taken = steps[0][2]
    tile = hike_map[curr_cord[0]][curr_cord[1]]

    if tile in ["^","v","<", ">"]:
        slope_cord = slope(hike_map,curr_cord[0],curr_cord[1])
        hike_map[curr_cord[0]][curr_cord[1]] = "O"
        curr_cord = slope_cord
        steps_taken += 1

    neighbors = getValidNeighbors(hike_map,curr_cord[0],curr_cord[1])

    hike_map[curr_cord[0]][curr_cord[1]] = "O"
    if len(neighbors) == 1:
        steps.insert(1,[hike_map,neighbors[0],steps_taken+1])
    elif len(neighbors) > 1:
        for neigh in neighbors:
            steps.insert(1,[copy.deepcopy(hike_map),neigh,steps_taken+1])
    elif longest < steps_taken+1:
        longest = steps_taken+1
        
    steps = steps[1::]
print(f"Day 23 part 1 answer: {longest}")