example_data = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]

with open("2025/Day1/day1_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

use_real_data = True
if not use_real_data:
    lines = example_data

rotations = [int(line[1:]) if line[0] == 'R' else -int(line[1:]) for line in lines]

solution = 0
pos = 50

for rotation in rotations:
    rel_pos = (pos + rotation)
    if rel_pos >= 100:
        solution += rel_pos // 100
    elif rel_pos <= 0:
        solution += (-rel_pos) // 100
        if pos != 0:
            solution += 1
    #print(f"{pos}, {rotation} -> {rel_pos % 100} | total {solution}")
    pos = rel_pos % 100


print(solution)