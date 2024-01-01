example = ['rn=1','cm-','qp=3','cm=2','qp-','pc=4','ot=9','ab=5','pc-','pc=6','ot=7']

with open("2023\Day15\day15_input.txt", "r") as f:
    sequence = f.readline().split(",")
    

use_real_data = True
if not use_real_data:
    sequence = example

def valueCalc(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value*17) % 256
    return value

total = 0
for step in sequence:
    total += valueCalc(step)
print(f"Part 1 answer: {total}")
