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

    while len(region_queue) > 0:
        r, c = region_queue.pop()
        region_area += 1
        seen.add((r,c))

        for v_r, v_c in vectors:
            neigh_r = r + v_r
            neigh_c = c + v_c    
            if not (0<=neigh_r<ROWS and 0<=neigh_c<COLS):
                region_perimeter += 1
                continue

            if garden[neigh_r][neigh_c] != garden[r][c]:
                region_perimeter += 1
                queue.add((neigh_r,neigh_c))
                
            elif (neigh_r, neigh_c) not in seen:
                region_queue.add((neigh_r,neigh_c))
    cost += region_area * region_perimeter
    
print("Day 10 part 1:" , cost)