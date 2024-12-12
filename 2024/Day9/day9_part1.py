example = "2333133121414131402"
example = list(map(int, example))

with open("2024/Day9/day9_input.txt", "r") as f:
    map = list(map(int, f.read().strip()))

use_real_data = True
if not use_real_data:
    map = example

rearranged_map = []
for i in range(len(map)):
    if i%2 == 0:
        rearranged_map.extend(map[i] * [i//2])
    else:
        rearranged_map.extend(map[i] * [-1])

i = 0
j = len(rearranged_map)-1
while i <= j:
    left = rearranged_map[i]
    right = rearranged_map[j]
    if left == right == -1:
        j -= 1
    elif left == -1 and right != -1:
        rearranged_map[i], rearranged_map[j] = right, left
        i += 1
        j -= 1
    elif left != -1 and right != -1:
        i += 1
    else:
        i += 1
        j -= 1 

print("Day 9 part 1:", sum(i*rearranged_map[i] for i in range(len(rearranged_map)) if rearranged_map[i] != -1))