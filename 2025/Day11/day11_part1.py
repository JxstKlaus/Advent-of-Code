example_data = [
    "aaa: you hhh",
    "you: bbb ccc",
    "bbb: ddd eee",
    "ccc: ddd eee fff",
    "ddd: ggg",
    "eee: out",
    "fff: out",
    "ggg: out",
    "hhh: ccc fff iii",
    "iii: out"
]

with open("2025/Day11/day11_input.txt", "r") as f:
    lines = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    lines = example_data

paths = {}
for line in lines:
    parent, childs = line.split(": ")
    childs = childs.split(" ")
    paths[parent] = childs

start = "you"
end = "out"

# number of paths from start to end

def find_paths(start):
    if start == end:
        return 1
    
    return sum(find_paths(child) for child in paths[start])

print(find_paths(start))