import re

example = [
    ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"],
    ["brwrr","bggr","gbbr","rrbgbr","ubwu","bwurrg","brgr","bbrgwb"]
]


with open("2024/Day19/day19_input.txt", "r") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.strip("\n").split(", ")
    designs = designs.split("\n")

use_real_data = False
if not use_real_data:
    patterns = example[0]
    designs = example[1]

def count_combinations(design, patterns):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for p in patterns:
            if design[i - len(p):i] == p and i >= len(p):
                dp[i] += dp[i - len(p)]
                
    return dp[len(design)]

print("Day 19 part 2:", sum([count_combinations(x, patterns) for x in designs]))