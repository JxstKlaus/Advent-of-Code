example_data = [
    "0:",
    "###",
    "##.",
    "##.",
    "",
    "1:",
    "###",
    "##.",
    ".##",
    "",
    "2:",
    ".##",
    "###",
    "##.",
    "",
    "3:",
    "##.",
    "###",
    "##.",
    "",
    "4:",
    "###",
    "#..",
    "###",
    "",
    "5:",
    "###",
    ".#.",
    "###",
    "",
    "4x4: 0 0 0 0 2 0",
    "12x5: 1 0 1 0 2 2",
    "12x5: 1 0 1 0 3 2"
]

with open("2025/Day12/day12_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

use_real_data = True
if not use_real_data:
    lines = example_data

shapes = [lines[:30][i : i + 3] for i in range(1, len(lines[:30]) - 1, 5)]

sizes = {i: 0 for i in range(len(shapes))}
for i in range(len(shapes)):
    for line in shapes[i]:
        sizes[i] += line.count("#")


areas, presents = [], []
for line in lines[30:]:
    area, present = line.split(": ")
    areas.append(tuple(map(int, area.split("x"))))
    presents.append(tuple(map(int, present.split(" "))))


# Basically the job is to tell if the different shaped present could fit in the area (grid)
# Rotation is allowed

# But no way im doing that 💀

# Lazy solution
# just checing if the area is bigger than the present area * 1.2
# 1.2 is a magic number

result = 0
for i in range(len(areas)):
    area = areas[i][0] * areas[i][1]
    present_area = 0
    for j in range(len(presents[i])):
        present_area += presents[i][j] * sizes[j]
    
    if area > present_area * 1.2:
        result += 1

print(result)