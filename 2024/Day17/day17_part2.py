example_data = [
    "Register A: 729",
    "Register B: 0",
    "Register C: 0",
    "",
    "Program: 0,1,5,4,3,0"
]

with open("2024/Day17/day17_input.txt", "r") as f:
    data = [x.strip() for x in f]

use_real_data = True
if not use_real_data:
    data = example_data

#parsing
computer = {}
computer["A"] = int(data[0].split(": ")[1])
computer["B"] = int(data[1].split(": ")[1])
computer["C"] = int(data[2].split(": ")[1])
computer["P"] = list(map(int, data[4].split(": ")[1].split(",")))

def handle_instruction(computer, ins, input, pointer):
    combo = {
        0:0,
        1:1,
        2:2,
        3:3,
        4:computer["A"],
        5:computer["B"],
        6:computer["C"],
    }
    output = -1

    if ins == 0:
        computer["A"] = computer["A"] // (2**combo[input])
    elif ins == 1:
        computer["B"] ^= input
    elif ins == 2:
        computer["B"] = combo[input]%8
    elif ins == 3:
        pointer = input-2 if computer["A"] != 0 else pointer
    elif ins == 4:
        computer["B"] ^= computer["C"]
    elif ins == 5:
        output = combo[input]%8
    elif ins == 6:
        computer["B"] = computer["A"] // (2**combo[input])
    elif ins == 7:
        computer["C"] = computer["A"] // (2**combo[input])

    pointer += 2

    return computer, output, pointer

def run_program(computer):
    program = computer["P"]
    pointer = 0
    final_output = []
    while pointer < len(program):
        computer, output, pointer = handle_instruction(computer, program[pointer], program[pointer+1], pointer)
        if output != -1:
            final_output.append(output)
    return final_output

candidates = [0]
for length in range(len(computer["P"])):
    next_candidates = []
    for val in candidates:
        for i in range(8):
            target = (val * 8) + i
            new_computer = computer.copy()
            new_computer["A"] = target
            if run_program(new_computer) == computer["P"][-length - 1 :]:
                next_candidates.append(target)
    candidates = next_candidates

print("Day 17 part 2:", min(candidates))