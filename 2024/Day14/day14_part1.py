import re
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


for _ in range(100):
    for i, (pos_c, pos_r, v_c, v_r) in enumerate(robots):
        robots[i][0] = (pos_c + v_c ) % COLS
        robots[i][1] = (pos_r + v_r) % ROWS

robot_count = [0,0,0,0]
COLS_mid = COLS//2
ROWS_mid = ROWS//2

for pos_c, pos_r, v_c, v_r in robots:
    if pos_r < ROWS_mid and pos_c < COLS_mid:
        robot_count[0] += 1
    elif pos_r < ROWS_mid and COLS_mid < pos_c < COLS+1:
        robot_count[1] += 1
    elif ROWS_mid < pos_r < ROWS and pos_c < COLS_mid:
        robot_count[2] += 1
    elif ROWS_mid < pos_r < ROWS and COLS_mid < pos_c < COLS+1:
        robot_count[3] += 1

safety = 1
for x  in robot_count:
    safety *= x

print("Day 14 part 1:", safety)