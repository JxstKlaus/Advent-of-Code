example_data = [
[
    (3, 5),
    (10, 14),
    (16, 20),
    (12, 18)
],

[1, 5, 8, 11, 17, 32]
]

with open("2025/Day5/day5_input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")
    ranges = [tuple(map(int, x.split("-"))) for x in blocks[0].split("\n")]
    ids = [int(x) for x in blocks[1].split("\n")]

use_real_data = True
if not use_real_data:
    ranges, ids = example_data

# Part 1
count = 0
for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            count += 1
            break
print(count)

# Part 2
count = 0
ranges.sort(key=lambda x: x[0])
merged = [ranges[0]]

for start, end in ranges[1:]:
    last_start, last_end = merged[-1]

    # overlap or touch
    if start <= last_end:  
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

for start, end in merged:
    count += end - start + 1
print(count)
# 363658334731702 high