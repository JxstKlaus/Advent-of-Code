example_data = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

with open("2025/Day4/day4_input.txt", "r") as f:
    puzzle = [line.strip() for line in f.readlines()]

use_real_data = True
if not use_real_data:
    puzzle = example_data

def get_adjestent(pos):
    x, y = pos
    adjestent = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(puzzle[0]) and 0 <= ny < len(puzzle):
                adjestent.append((nx, ny))
    return adjestent


total = 0
for y in range(len(puzzle)):
    for x in range(len(puzzle[0])):
        if puzzle[y][x] == '@':
            adj = get_adjestent((x, y))
            count = sum(1 for (nx, ny) in adj if puzzle[ny][nx] == '@')
            if count < 4:
                total += 1
print(total)