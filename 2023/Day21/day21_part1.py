example = [
    '...........',
    '.....###.#.',
    '.###.##..#.',
    '..#.#...#..',
    '....#.#....',
    '.##..S####.',
    '.##..#...#.',
    '.......##..',
    '.##.#.####.',
    '.##..##.##.',
    '...........'
]

map = [row.strip() for row in open("2023\Day21\day21_input.txt", "r")]

use_real_data = True
if not use_real_data:
    map = example

for i,row in enumerate(map):
    if "S" in row:
        starting_point = (i,row.index("S"))
        map[starting_point[0]] = map[starting_point[0]].replace("S", ".")
        break

#return a list like [1,1,0,1] = [up,down,right,left]
#0: cant move
#1: can move
def checkValidMoves(x,y):
    valid_moves = []
    if (x-1 >= 0) and (x+1 <= len(map)-1) and (y+1 <= len(map[0])-1) and (y-1 >= 0):
        if map[x-1][y] == ".":
            valid_moves.append((x-1,y))
        if map[x+1][y] == ".":
            valid_moves.append((x+1,y))
        if map[x][y+1] == ".":
            valid_moves.append((x,y+1))
        if map[x][y-1] == ".":
            valid_moves.append((x,y-1))
    return valid_moves

steps_left = 64
reached_pots = []
queue = [[starting_point,steps_left]]

while queue != []:
    cord,steps_left = queue[0]
    for neigh in checkValidMoves(cord[0],cord[1]):
        if steps_left-1 == 0 and neigh not in reached_pots:
            reached_pots.append(neigh)
        elif steps_left-1 > 0 and [neigh,steps_left-1] not in queue:
            queue.append([neigh,steps_left-1])
    #print(f"From cord: {cord} | steps left: {steps_left} | can move to: {checkValidMoves(cord[0],cord[1])}")
    queue = queue[1::]

print(f"Day 21 part 1 answer: {len(reached_pots)}")
