
example = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]
example = [list(x) for x in example]

with open("2024/Day6/day6_input.txt", "r") as f:
    map = [list(x.strip()) for x in f]

use_real_data = True
if not use_real_data:
    map = example

#finding starting pos
for row in map:
    if "^" in row:
        start_pos = (map.index(row), row.index("^"))
        break

vectors = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]


current_pos = [start_pos[0], start_pos[1]]
i = 0
points_visited = 0

def is_visited(pos, map):
    return map[pos[0]][pos[1]] != "X"

while True:
    current_vect = vectors[i%4]
    next_pos = [current_pos[0] + current_vect[0], current_pos[1] + current_vect[1]]

    if next_pos[0] not in range(-1, len(map)) or next_pos[1] not in range(-1, len(map[0])):
        break
    elif map[next_pos[0]][next_pos[1]] == "#":
        i += 1
    else:
        current_pos = next_pos
        if is_visited(current_pos,map):
            points_visited += 1
            map[current_pos[0]][current_pos[1]] = "X"
    

print("Day 6 part 1:", points_visited)