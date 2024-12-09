import re
example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("2024/Day3/day3_input.txt", "r") as f:
    memory = "".join([x.strip() for x in f])

use_real_data = True
if not use_real_data:
    memory = example

total = 0
pattern = r"don't\(\)(.*?)(do\(\)|$)"
line = re.sub(pattern, "", memory)

mul_strings = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
for mul in mul_strings:
    num1, num2 = mul[4:-1].split(",")
    total += (int(num1) * int(num2))

print("Day 3 part 2 answer:", total)