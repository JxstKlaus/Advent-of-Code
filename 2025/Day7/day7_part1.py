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

start_col = map[0].index('S')

coords = set([start_col])
splits = 0
for row in map:
    new_coords = set()
    for coord in coords: 
        if row[coord] == '^':
            splits += 1
            new_coords.add(coord - 1)  # go left
            new_coords.add(coord + 1)  # go right
        else:
            new_coords.add(coord)  # continue down
    coords = new_coords

print(splits)