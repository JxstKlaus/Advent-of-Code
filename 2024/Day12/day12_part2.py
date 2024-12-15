from collections import deque

example = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]

example = [list(x) for x in example]

with open("2024/Day12/day12_input.txt", "r") as f:
    garden = [list(x.strip()) for x in f.readlines()]

use_real_data = True
if not use_real_data:
    garden = example

garden_coords = {}
for x in range(len(garden)):
    for y in range(len(garden[0])):
        garden_coords[(x,y)] = garden[x][y]

vectors = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]

ROWS = len(garden)
COLS = len(garden[0])

seen = set()

queue = set()
queue.add((0,0))
cost = 0
while len(queue) > 0:
    region_queue = set()
    next = queue.pop()
    if next not in seen:
        region_queue.add(next)

    region_area = 0
    region_perimeter = 0
    perim_coords = dict()

    while len(region_queue) > 0:
        r, c = region_queue.pop()
        region_area += 1
        seen.add((r,c))

        for v_r, v_c in vectors:
            neigh_r = r + v_r
            neigh_c = c + v_c

            is_in_range = True
            is_neigh_same_type = True
            if not (0<=neigh_r<ROWS and 0<=neigh_c<COLS):
                is_in_range = False

            elif not(garden[neigh_r][neigh_c] == garden[r][c]):
                is_neigh_same_type = False
                queue.add((neigh_r,neigh_c))

            elif (neigh_r, neigh_c) not in seen:
                region_queue.add((neigh_r,neigh_c))


            if not is_in_range or not is_neigh_same_type:
                region_perimeter += 1
                #part 2
                # side = same direction, adjacent
                if (v_r,v_c) not in perim_coords:
                    perim_coords[(v_r,v_c)] = set()
                perim_coords[(v_r,v_c)].add((r,c))
    #part 2
    #iterating through perimeter coords with same direction 
    #since the total perimeter was already calculated from part 1 I work backwards
    #lets say (x1,y1) is the pivot element. For every pivot I try to find out if there is a neighbor looking the same direction
    #if yes then I decrement region_perimetre by 1

    for k, values in perim_coords.items():
        values = list(values)
        for i,(x1,y1) in enumerate(values):
            for x2,y2 in values[i:]:
                if x1 == x2 and abs(y2-y1) == 1:
                    region_perimeter -= 1
                    
                elif y1 == y2 and abs(x2-x1) == 1:
                    region_perimeter -= 1

    cost += region_area * region_perimeter


    
print("Day 10 part 2:" , cost)