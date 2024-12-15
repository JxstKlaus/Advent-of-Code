import re
from collections import deque
example = [
    [0,4, 3,-3],
    [6,3, -1,-3],
    [10,3, -1,2],
    [2,0, 2,-1],
    [0,0, 1,3],
    [3,0, -2,-2],
    [7,6, -1,-3],
    [3,0, -1,-2],
    [9,3, 2,3],
    [7,3, -1,2],
    [2,4, 2,-3],
    [9,5, -3,-3]
]

with open("2024/Day14/day14_input.txt", "r") as f:
    data = [line.strip() for line in f]
    robots = []
    for line in data:
        numbers = re.findall(r'-?\d+', line)
        numbers = list(map(int, numbers))
        robots.append(numbers)

ROWS = 103
COLS = 101

use_real_data = True
if not use_real_data:
    robots = example
    ROWS = 7
    COLS = 11

COLS_mid = COLS//2
ROWS_mid = ROWS//2

vectors = [ (-1,0), (0,1), (1,0), (0,-1)]

def bfs(start, visited):
        queue = deque([start])
        group = set([start])
        visited.add(start)

        while queue:
            r, c = queue.popleft()
            for v_r, v_c in vectors:
                neighbor = (r + v_r, c + v_c)
                if neighbor in robot_positions and neighbor not in visited:
                    visited.add(neighbor)
                    group.add(neighbor)
                    queue.append(neighbor)
        return group

iteration = 0
found_tree = False
while not found_tree:
    iteration += 1
    for i, (pos_c, pos_r, v_c, v_r) in enumerate(robots):
        robots[i][0] = (pos_c + v_c ) % COLS
        robots[i][1] = (pos_r + v_r) % ROWS

    #part2:
    #checking for largest cluster of points stuck together in every iteration
    #if its above a certain treshold then tree found (hopefully)
    robot_positions = set([(r[1], r[0]) for r in robots])

    visited = set()
    largest_group = set()

    for pos in robot_positions:
        if pos not in visited:
            group = bfs(pos, visited)
            if len(group) > len(largest_group):
                largest_group = group

    #draw grid
    if len(largest_group) > len(robot_positions)/5:
        print("Day 14 part 2: Found at iteration", iteration)
        grid = []
        for x in range(ROWS):
            row = []
            for y in range(COLS):
                row.append(".")
            grid.append(row)
        for x,y in robot_positions:
            grid[x][y] = "#"
        for x in grid:
            print(''.join(x))

        found_tree = True