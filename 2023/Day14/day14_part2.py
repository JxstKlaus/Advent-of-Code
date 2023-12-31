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
    return ["".join([pattern[y][x] for y in range(len(pattern))][::-1]) for x in range(len(pattern[0]))]





def tiltPlatform(platform):   
    for _ in range(4):
        new_platform = platform
        for i,line in enumerate(rotatePlatform(new_platform)):
            line = line.split("#")
            for l,part in enumerate(line):
                line[l] = part.count(".") * "." + part.count("O") * "O"
            #print("#".join(line))
            new_platform[i] = "#".join(line)
    return new_platform


original_platform = platform

cache = []
for x in range(200):  
    platform = tiltPlatform(platform)
    joined = ''.join(platform)
    if joined in cache:
        sequence_end = x
        break
    cache.append(joined)


sequence_start = cache.index("".join(platform))

index = (1000000000 - sequence_start - 1) % (sequence_end - sequence_start)
    
for x in range(index):  
    platform = tiltPlatform(original_platform)

total_load = 0
for l,line in enumerate(platform):
    for i,char in enumerate(line):
        if char == "O":
            total_load += len(platform) - l
    print(line)

print(f"Part 2 answer: {total_load}")