from functools import lru_cache

example_data = [
    "svr: aaa bbb",
    "aaa: fft",
    "fft: ccc",
    "bbb: tty",
    "tty: ccc",
    "ccc: ddd eee",
    "ddd: hub",
    "hub: fff",
    "eee: dac",
    "dac: fff",
    "fff: ggg hhh",
    "ggg: out",
    "hhh: out"
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


start = "svr"
end = "out"
must_visit = ("dac", "fft")


# number of paths from start to end with must visited nodes
@lru_cache(None)
def find_paths(start, visited_req):
    if start in must_visit and start not in visited_req:
        visited_req += (start,)

    if start == end:
        return 1 if all([x in visited_req for x in must_visit]) else 0

    return sum(
        find_paths(child, visited_req)
        for child in paths.get(start, [])
    )

count = find_paths(start, tuple())
print(count)