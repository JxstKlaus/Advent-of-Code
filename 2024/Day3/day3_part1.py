import re
example = [
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
]

with open("2024/Day3/day3_input.txt", "r") as f:
    memory = [x.strip() for x in f]

use_real_data = True
if not use_real_data:
    memory = example

total = 0
for line in memory:
    line = line.split('mul')
    for segment in line:
        segment = segment.split(",")
        if segment[0][0] == "(" and segment[0][1::].isdigit() and segment[1].split(")")[0].isdigit():
            total += int(segment[0][1::]) * int(segment[1].split(")")[0])
print("Day 3 part 1 answer:", total)