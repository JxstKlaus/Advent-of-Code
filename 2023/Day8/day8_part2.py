from math import lcm

example = [
["LR"],
[''],
['11A', '(11B, XXX)'],
['11B', '(XXX, 11Z)'],
['11Z', '(11B, XXX)'],
['22A', '(22B, XXX)'],
['22B', '(22C, 22C)'],
['22C', '(22Z, 22Z)'],
['22Z', '(22B, 22B)'],
['XXX', '(XXX, XXX)']
]

with open("Day8\day8_input.txt", "r") as f:
    data = [line.strip().split(" = ") for line in f]

use_real_data = True
if not use_real_data:
    data = example

instructions = data[0][0]
nodes = data[2:]

ways = {node[0]: {"L": node[1][1:4], "R": node[1][6:9]} for node in nodes}

#all nodes that end with "A"
positions = [way[0] for way in nodes if way[0][-1] == "A"] 

#counting the steps from each position to the first node that ends with "Z"
all_steps = [[]] * len(positions)

for i,pos in enumerate(positions):
    current_steps = 0
    instructions = data[0][0]
        
    while pos[-1] != "Z":
        for dir in instructions:  
            current_steps += 1
            pos = ways[pos][dir]
            if pos[-1] == "Z":
                break
            instructions = instructions[1:] + instructions[0]

    all_steps[i] = current_steps

print(f"Part 2 answer: {lcm(*all_steps)}")

