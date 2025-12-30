example_data = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]

with open("2025/Day7/day7_input.txt", "r") as f:
    map = [line.strip() for line in f.readlines()]

use_real_data = True
if not use_real_data:
    map = example_data

start_col = map[0].index("S")
rows, cols = len(map), len(map[0])

# path_map[row][col] -> number of ways to reach (row, col)
path_map = [[0] * cols for _ in range(len(map))]
path_map[0][start_col] = 1

for row in range(rows-1):
    for col in range(cols):
        if path_map[row][col] == 0:
            continue

        ways = path_map[row][col]

        if map[row][col] == '^':
            path_map[row + 1][col - 1] += ways
            path_map[row + 1][col + 1] += ways
        else:
            path_map[row + 1][col] += ways

# total ways to reach bottom row
timelines = sum(path_map[rows - 1])
print(timelines)