example = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

with open("2024/Day8/day8_input.txt", "r") as f:
    map = [x.strip() for x in f]

use_real_data = True
if not use_real_data:
    map = example


ROWS = len(map)
COLS = len(map[0])
antennas = {}
antinodes = set()

for r in range(ROWS):
    for c in range(COLS):
        tile = map[r][c]
        if tile != ".":
            antinodes.add((r,c))
            if tile in antennas:
                antennas[tile].append((r,c))
            else:
                antennas[tile] = [(r,c)]

#for every same frequncy antenna 2 antinodes are created
#i.e. A1(1,1) and A2(2,2) --> distance between them: DIST(x2-x1, y2-y1) antinode positions: A1 - DIST and A2 + DIST

for freq in antennas:
    for i,(x1,y1) in enumerate(antennas[freq][:-1]):
        new_antinodes = set()
        for x2,y2 in antennas[freq][i+1:]:
            dist_x, dist_y = x2-x1, y2-y1

            anti1_x = x1 - dist_x
            anti1_y = y1 - dist_y

            anti2_x = x2 + dist_x
            anti2_y = y2 + dist_y

            #adding while loop to calculate further distances until they are in map boundaries
            while 0 <= anti1_x < ROWS and (0 <= anti1_y < COLS):
                antinodes.add((anti1_x, anti1_y))
                anti1_x -= dist_x
                anti1_y -= dist_y
                
            while 0 <= anti2_x < ROWS and 0 <= anti2_y < COLS:
                antinodes.add((anti2_x, anti2_y))
                anti2_x += dist_x
                anti2_y += dist_y
                
print("Day 8 part 2:", len(antinodes))