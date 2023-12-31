example = [
"O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#...."]

with open("2023\Day14\day14_input.txt", "r") as f:
    platform = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    platform = example


def rotatePlatform(pattern):
    return ["".join([pattern[y][x] for y in range(len(pattern))]) for x in range(len(pattern[0]))][::-1]

for i,line in enumerate(rotatePlatform(platform)):
    line = line.split("#")
    for l,part in enumerate(line):
        line[l] = part.count("O") * "O" + part.count(".") * "."
    #print("#".join(line))
    platform[i] = "#".join(line)
            

total_load = 0
for line in platform:
    for i,char in enumerate(line):
        if char == "O":
            total_load += len(line) - i
print(f"Part 1 answer: {total_load}")