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

use_real_data = True
if not use_real_data:
    galaxy_map = example


#swaps rows and columns
def transposeMap(map):
    return ["".join([map[y][x] for y in range(len(map))]) for x in range(len(map[0]))]

#returns a list that indicates the empty rows and columns betwwn 2 cord
def emptySpace(map,cord1,cord2):
    empty_space = [0,0]
    x_start = min([cord1[0],cord2[0]])
    x_end = x_start + abs(cord1[0] - cord2[0])
    
    for row in map[x_start:x_end+1]:
        if "#" not in row:
            empty_space[0] += 1

    y_start = min([cord1[1],cord2[1]])
    y_end = y_start + abs(cord1[1] - cord2[1])


    for col in transposeMap(map)[y_start:y_end+1]: 
        if "#" not in col:
            empty_space[1] += 1

    return empty_space



#finds the coordinates of all galaxies
galaxy_cords = []
for x,row in enumerate(galaxy_map):
    for y,char in enumerate(row):
        if char == "#":
            galaxy_cords.append((x,y))


#calculates the distance between 2 given galaxies
def calcDistance(cord1: tuple,cord2: tuple):
    empty = emptySpace(galaxy_map, cord1, cord2)
    x_empty = empty[0] * 1000000
    y_empty = empty[1] * 1000000
    return (abs(cord1[0] - cord2[0]) - empty[0] + x_empty) + (abs(cord1[1] - cord2[1]) - empty[1] + y_empty)

#sums the distances

print(len(galaxy_cords))
total_dist = 0
for i,cord1 in enumerate(galaxy_cords):
    print(i)
    for cord2 in galaxy_cords[i+1::]:
        #print(cord1,cord2,calcDistance(cord1,cord2))
        total_dist += calcDistance(cord1,cord2)
print(f"Part 2 answer: {total_dist}")



"""print(emptySpace(galaxy_map, (0,3), (2,0)))
for x in galaxy_map:
    print(x)
print("\n")
for x in transposeMap(galaxy_map):
    print(x)"""