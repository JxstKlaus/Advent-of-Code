example = [[
    "########",
    "#..O.O.#",
    "##@.O..#",
    "#...O..#",
    "#.#.O..#",
    "#...O..#",
    "#......#",
    "########"
], "<^^>>>vv<v>>v<<"]

with open("2024/Day15/day15_input.txt", "r") as f:
    data = f.read().strip().split("\n\n")
    map_list = [list(x) for x in data[0].split("\n")]
    instruction_list = data[1].replace("\n", "")

use_real_data = True
if not use_real_data:
    map_list = [list(x) for x in example[0]]
    instruction_list = example[1]

instructions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

robot_coord = None
for y, row in enumerate(map_list):
    for x, col in enumerate(row):
        if col == "@":
            robot_coord = (x, y)
            break

WIDTH = len(map_list[0])
HEIGHT = len(map_list)

def is_box(x,y):
    return map_list[x][y] == "O"

def is_wall(x,y):
    return map_list[x][y] == "#"

def check_for_box(x,y, dx, dy):
    new_x = (x + dx)
    new_y = (y + dy)
    return is_box(new_x, new_y)

def push_box(x, y, new_x, new_y):
    map_list[new_x][new_y] = "O"
    map_list[x][y] = "."

def move(x, y, dx, dy):
    new_x = (x + dx)
    new_y = (y + dy)
    
    #no move if next tile is wall
    if is_wall(new_x, new_y):
        return x, y
    
    #checking for box
    box_count = 0
    box_x = x
    box_y = y
    while check_for_box(box_x, box_y, dx, dy):
        box_x += dx
        box_y += dy
        box_count += 1
    
    #if the tile after last box is wall then no move
    after_box_x = box_x + dx
    after_box_y = box_y + dy

    if is_wall(box_x+dx, box_y+dy):
        return x, y
    
    #pushing box if present
    if box_count > 0:
        if map_list[after_box_x][after_box_y] == ".":
            push_box(new_x, new_y, after_box_x, after_box_y)
        else:
            return x, y

    #moving robot
    map_list[new_x][new_y] = "@"
    map_list[x][y] = "."

    return new_x, new_y


for ins in instruction_list:
    dx,dy = instructions[ins]
    x, y = move(robot_coord[0], robot_coord[1], dx, dy)
    robot_coord = (x, y)

for tiles in map_list:
    print("".join(tiles))


total = 0
for x in range(HEIGHT):
    for y in range(WIDTH):
        if map_list[x][y] == "O":
            total += x*100 + y

print("Day 15 part 1:", total)