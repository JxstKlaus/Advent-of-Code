import re, itertools

example_data = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]

with open("2025/Day10/day10_input.txt", "r") as f:
    lines = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    lines = example_data

total = 0
for line in lines:
    match = re.match(r"\[(.*)\] ([()\d, ]*) \{(.*)\}", line)
    target, buttons, _ = match.groups()

    target = {i for i in range(len(target)) if target[i] == "#"}
    buttons = [set(map(int, btn[1:-1].split(","))) for btn in buttons.split(" ")]
    
    for i in range(1, len(buttons)):
        combinations = itertools.combinations(buttons, i)
        for combination in combinations:
            state = set()
            for button in combination:
                state ^= button
            if state == target:
                break
        else:
            continue
        total += i
        break

print(total)
