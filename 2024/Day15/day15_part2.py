example = [[
    "##########",
    "#..O..O.O#",
    "#......O.#",
    "#.OO..O.O#",
    "#..O@..O.#",
    "#O#..O...#",
    "#O..O..O.#",
    "#.OO.O.OO#",
    "#....O...#",
    "##########"
], "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"]

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

def make_map_2x_wide(map_list):
    new_map = []
    for row in map_list:
        new_row = []
        for col in row:
            if col == ".":
                new_row.extend([".","."])
            elif col == "#":
                new_row.extend(["#","#"])
            elif col == "@":
                new_row.extend(["@","."])
            elif col == "O":
                new_row.extend(["[","]"])
        new_map.append(new_row)
    return new_map

map_list = make_map_2x_wide(map_list)

robot_coord = None
for x, row in enumerate(map_list):
    for y, col in enumerate(row):
        if col == "@":
            robot_coord = (x, y)
            break

WIDTH = len(map_list[0])
HEIGHT = len(map_list)

def is_box(x,y):
    return map_list[x][y] == "[" or map_list[x][y] == "]"

def is_wall(x,y):
    return map_list[x][y] == "#"

def get_box_positions(x,y, dx, dy):
    box_positions = set()
    if dx == 0: #horizontal move
        while is_box(x+dx, y+dy):
            box_positions.add((x+dx, y+dy))
            x += dx
            y += dy
    else: #vertical move
        box_layer_positions = set([(x, y)])
        while box_layer_positions:
            new_box_layer_positions = set()
            for x,y in box_layer_positions:
                if map_list[x+dx][y+dy] == "[":
                    box_positions.add((x+dx, y+dy))
                    box_positions.add((x+dx, y+dy+1))

                    new_box_layer_positions.add((x+dx, y+dy))
                    new_box_layer_positions.add((x+dx, y+dy+1))
                elif map_list[x+dx][y+dy] == "]":
                    box_positions.add((x+dx, y+dy))
                    box_positions.add((x+dx, y+dy-1))

                    new_box_layer_positions.add((x+dx, y+dy))
                    new_box_layer_positions.add((x+dx, y+dy-1))

            box_layer_positions = new_box_layer_positions

    return box_positions

def can_move(box_positions, dx, dy):
    for box_x, box_y in box_positions:
        if is_wall(box_x+dx, box_y+dy):
            return False
    return True

def push_boxes(box_positions, dx, dy):
    # Store old box positions with tile for easier replacement
    box_tile_positions_dict = {}
    for box_x, box_y in box_positions:
        box_tile_positions_dict[(box_x, box_y)] = map_list[box_x][box_y]
        map_list[box_x][box_y] = "."
    
    for box_x, box_y in box_positions:
        map_list[box_x+dx][box_y+dy] = box_tile_positions_dict[(box_x, box_y)]

def move(x, y, dx, dy):
    new_x = (x + dx)
    new_y = (y + dy)
    
    #no move if next tile is wall
    if is_wall(new_x, new_y):
        return x, y
    
    #getting positions for boxes
    box_positions = get_box_positions(x, y, dx, dy)

    #no move if boxes cannot be pushed
    if not can_move(box_positions, dx, dy):
        return x, y
    
    #moving boxes
    push_boxes(box_positions, dx, dy)

    #moving robot
    map_list[new_x][new_y] = "@"
    map_list[x][y] = "."
    return new_x, new_y


for ins in instruction_list:
    dx,dy = instructions[ins]
    x, y = move(robot_coord[0], robot_coord[1], dx, dy, ins)
    robot_coord = (x, y)

total = 0
for x in range(HEIGHT):
    for y in range(WIDTH):
        if map_list[x][y] == "[":
            total += x*100 + y

print("Day 15 part 2:", total)