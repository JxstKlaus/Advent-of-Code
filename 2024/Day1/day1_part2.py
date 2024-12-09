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

similarity_list = {}
for num in right:
    if num in similarity_list:
        similarity_list[num] += 1
    else:
        similarity_list[num] = 1


print(sum([similarity_list[num]*num for num in left if num in similarity_list]))