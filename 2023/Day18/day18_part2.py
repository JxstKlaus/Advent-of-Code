example = [
    ['R', 6],
    ['D', 5],
    ['L', 2],
    ['D', 2],
    ['R', 2],
    ['D', 2],
    ['L', 5],
    ['U', 2],
    ['L', 1],
    ['U', 2],
    ['R', 2],
    ['U', 3],
    ['L', 2],
    ['U', 2]
]
with open("2023\Day18\day18_input.txt", "r") as f:
    data = [line.strip().split(" ") for line in f]
    data = [[(x[0], int(x[1])), x[2][2:-1]] for x in data]

directions = {0:"R", 1:"D", 2:"L", 3:"U"}

#parsing new instructions
instructions = [[directions[int(line[1][-1])], int(line[1][:-1],16)] for line in data]

use_real_data = True
if not use_real_data:
    plan = example

#Since the last instruction ends up where the first one started
#I manually added the last instruction to the first place and the first one to the last place to prevent hiccups

x_pos = 0
y_pos = 0

instructions = [instructions[-1]] + instructions + [instructions[0]]
cords = [(0,0)]

#This algorithm prepares the coordinates for the Gauss' shoelace formula
#They had to be modified in order to get the answer

#Imagine a grid
#The cartesian coordinates (and also the area, shape, etc...) are different when you mark the area out by follow the orders by coloring the 1x1 squares and 
#when you follow the instructions by drawing a line on the edges of the grid 
#Basically this program builds a fence around the shape (hole) if that makes sense

for bef,ins,aft in zip(instructions[:-2],instructions[1:-1],instructions[2:]):
    match ins[0]:
        case "U":
            if bef[0] == "R" and aft[0] == "L":
                x_pos += (ins[1]-1)
            if bef[0] == "L" and aft[0] == "R":
                x_pos += (ins[1]+1)
            elif bef[0] == aft[0]:
                x_pos += ins[1]

        case "D":
            if bef[0] == "L" and aft[0] == "R":
                x_pos -= (ins[1]-1)
            if bef[0] == "R" and aft[0] == "L":
                x_pos -= (ins[1]+1)
            elif bef[0] == aft[0]:
                 x_pos -= ins[1]

        case "R":
            if bef[0] == "U" and aft[0] == "D":
                y_pos += (ins[1] +1)
            elif bef[0] == "D" and aft[0] == "U":
                y_pos += (ins[1] - 1)
            elif bef[0] == aft[0]:
                 y_pos += ins[1]        
    
        case "L":
            if bef[0] == "D" and aft[0] == "U":
                y_pos -= (ins[1] +1)
            elif bef[0] == "U" and aft[0] == "D":
                y_pos -= (ins[1] -1)
            elif bef[0] == aft[0]:
                 y_pos -= ins[1]
            else:
                y_pos -= ins[1]
            
    cords.append((y_pos,x_pos))

area = 0
for (x1,y1),(x2,y2) in zip(cords[:-1],cords[1::]):
    area += x1 * y2
    area -= x2 * y1

print(f"Day 18 part 2 answer: {abs(area) // 2}")