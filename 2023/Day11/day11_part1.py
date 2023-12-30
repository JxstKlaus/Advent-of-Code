example = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]

with open("Day11\day11_input.txt", "r") as f:
    galaxy_map = [line.strip() for line in f]

use_real_data = False
if not use_real_data:
    galaxy_map = example


#swaps rows and columns
def transposeMap(map):
    return ["".join([map[y][x] for y in range(len(map))]) for x in range(len(map[0]))]

#expands the empty lines
def expandMap(map):
    empty_space = "." * len(map[0])
    expanded_map = []

    for row in map:
        if "#" not in row:
            expanded_map.append(empty_space)
        expanded_map.append(row)
    
    map = transposeMap(expanded_map)
    empty_space = "." * len(map[0])
    expanded_map = []

    for row in map:
        if "#" not in row:
            expanded_map.append(empty_space)
        expanded_map.append(row)
    return transposeMap(expanded_map)

exp_galaxy_map = expandMap(galaxy_map)

#finds the coordinates of all galaxies
galaxy_cords = []
for x,row in enumerate(exp_galaxy_map):
    for y,char in enumerate(row):
        if char == "#":
            galaxy_cords.append((x,y))

#calculates the distance between 2 given galaxies
def calcDistance(cord1: tuple,cord2: tuple):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])

#sums the distances
total_dist = 0
for i,cord1 in enumerate(galaxy_cords):
    for cord2 in galaxy_cords[i+1::]:
        total_dist += calcDistance(cord1,cord2)
print(f"Part 1 answer: {total_dist}")



