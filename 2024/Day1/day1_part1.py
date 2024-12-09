example = [
    [3,4,2,1,3,3],
    [4,3,5,3,9,3]
]



with open("2024/Day1\day1_input.txt", "r") as f:
    left,right = [], []
    for line in f:
        line = line.strip().split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

use_real_data = True
if not use_real_data:
    left, right = example[0], example[1]

left.sort()
right.sort()

print(sum([abs(num1-num2) for num1, num2 in zip(left,right)]))