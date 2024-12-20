import re

example = [
    ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"],
    ["brwrr","bggr","gbbr","rrbgbr","ubwu","bwurrg","brgr","bbrgwb"]
]


with open("2024/Day19/day19_input.txt", "r") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.strip("\n").split(", ")
    designs = designs.split("\n")

use_real_data = True
if not use_real_data:
    patterns = example[0]
    designs = example[1]

def can_create_pattern(design, patterns):
    regex_pattern = "^(" + "|".join(map(re.escape, patterns)) + ")+$"
    return re.fullmatch(regex_pattern, design) is not None

#removing patterns that can be created using other patterns
patterns_by_length = {}
for pattern in patterns:
    if len(pattern) in patterns_by_length:
        patterns_by_length[len(pattern)].append(pattern)
    else:
        patterns_by_length[len(pattern)] = [pattern]

patterns_by_length = [patterns_by_length[x] for x in sorted(patterns_by_length.keys())]

new_patterns = patterns_by_length[0]
for i in range(len(patterns_by_length)-1):
    for ps in patterns_by_length[i+1:]:
        for p in ps:
            if not can_create_pattern(p, new_patterns):
                new_patterns.append(p)

print("Day 19 part 1:", len([x for x in designs if can_create_pattern(x, new_patterns)]))