import re
import numpy as np

example = [
    "Button A: X+94, Y+34",
    "Button B: X+22, Y+67",
    "Prize: X=8400, Y=5400",
    "",
    "Button A: X+26, Y+66",
    "Button B: X+67, Y+21",
    "Prize: X=12748, Y=12176",
    "",
    "Button A: X+17, Y+86",
    "Button B: X+84, Y+37",
    "Prize: X=7870, Y=6450",
    "",
    "Button A: X+69, Y+23",
    "Button B: X+27, Y+71",
    "Prize: X=18641, Y=10279"
]

with open("2024/Day13/day13_input.txt", "r") as f:
    data = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    data = example

#parsing
machines = []
for i in range(0,len(data),4):
    machine = {}
    machine["A"] = tuple(map(int, re.findall(r'X\+(\d+), Y\+(\d+)', data[i])[0]))
    machine["B"] = tuple(map(int, re.findall(r'X\+(\d+), Y\+(\d+)', data[i+1])[0]))
    machine["P"] = tuple(map(int, re.findall(r'X=(\d+), Y=(\d+)', data[i+2])[0]))
    machines.append(machine)

#Button A: X+94, Y+34   --> A1=94, A2 =34
#Button B: X+22, Y+67   --> B1=22, B2=67
#Prize: X=8400, Y=5400

#equation1: a*A1 + b*B1 = X
#equation2: a*A2 + b*B2 = Y

#a*94 + b*22 = 8400
#a*34 + b*67 = 5400


total = 0 
for machine in machines:
    has_solution = False
    a1,a2 = machine["A"]
    b1,b2 = machine["B"]
    p1 = machine["P"][0]+10000000000000
    p2 = machine["P"][1]+10000000000000

    #making a copy of equation1 for later
    original_a1 = a1
    original_b1 = b1
    original_p1 = p1

    #a1 and a2 should equal so that it can be eliminated
    a1 *= a2
    b1 *= a2
    p1 *= a2
    
    a2 *= original_a1
    b2*= original_a1
    p2 *= original_a1

    #substracting equation1 from equation2
    b3 = b2 - b1
    p3 = p2 - p1

    #if b_press is a whole number the equation has solution
    b_press = p3//b3
    if p3/b3 == b_press:
        has_solution = True
    if has_solution:
        a_press = (original_p1 - original_b1*b_press) // original_a1
        total += (a_press*3 + b_press)


print("Day 13 part 1:", total)

#438218984040623365 high