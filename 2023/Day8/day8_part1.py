example = [
    ['LLR'],
    [''],
    ['AAA', '(BBB, BBB)'],
    ['BBB', '(AAA, ZZZ)'],
    ['ZZZ', '(ZZZ, ZZZ)'],
]

with open("Day8\day8_input.txt", "r") as f:
    data = [line.strip().split(" = ") for line in f]

use_real_data = True
if not use_real_data:
    data = example

instructions = data[0][0]
nodes = data[2:]

ways = {node[0]: {"L": node[1][1:4], "R": node[1][6:9]} for node in nodes}

position = "AAA"
steps = 0

while position != "ZZZ":
    for dir in instructions:
        steps += 1
        position = ways[position][dir]
        if position =="ZZZ":
            break
        instructions = instructions[1:] + instructions[0]



print(f"Part 1 answer: {steps}")

