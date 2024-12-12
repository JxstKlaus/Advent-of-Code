from collections import deque 

example = [
    [8,9,0,1,0,1,2,3],
    [7,8,1,2,1,8,7,4],
    [8,7,4,3,0,9,6,5],
    [9,6,5,4,9,8,7,4],
    [4,5,6,7,8,9,0,3],
    [3,2,0,1,9,0,1,2],
    [0,1,3,2,9,8,0,1],
    [1,0,4,5,6,7,3,2]
]


with open("2024/Day10/day10_input.txt", "r") as f:
    map = [[int(y) for y in x.strip()] for x in f]

use_real_data = True
if not use_real_data:
    map = example

vectors = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]

ROWS = len(map)
COLS = len(map[0])

#finding all 0's position 
trailheads = []
for x in range(ROWS):
    for y in range(COLS):
        if map[x][y] == 0:
            trailheads.append((x,y))

scores = 0
for x,y in trailheads:
    queue = deque([(x,y)]) 
    seen = set()
    while len(queue) > 0:
        r, c = queue.pop()
        seen.add((r,c))
        if map[r][c] == 9:
            scores += 1
            continue
        for v_r, v_c in vectors:
            neigh_r = r + v_r
            neigh_c = c + v_c
            if 0<=neigh_r<ROWS and 0<=neigh_c<COLS:
                if (neigh_r, neigh_c) not in seen and map[neigh_r][neigh_c] - map[r][c] == 1:
                    queue.append((neigh_r,neigh_c))

print("Day 10 part 1:" ,scores)