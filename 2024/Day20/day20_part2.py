from collections import deque

example = [
    "###############",
    "#...#...#.....#",
    "#.#.#.#.#.###.#",
    "#S#...#.#.#...#",
    "#######.#.#.###",
    "#######.#.#...#",
    "#######.#.###.#",
    "###..E#...#...#",
    "###.#######.###",
    "#...###...#...#",
    "#.#####.#.###.#",
    "#.#...#.#.#...#",
    "#.#.#.#.#.#.###",
    "#...#...#...###",
    "###############"
]


with open("2024/Day20/day20_input.txt", "r") as f:
    map = [line.strip() for line in f]

use_real_data = True
if not use_real_data:
    map = example

def get_srart_end(map):
    for i in range(len(map)):
        if "S" in map[i]:
            start = (i, map[i].index("S"))
        if "E" in map[i]:
            end = (i, map[i].index("E"))
    return start, end

start, end = get_srart_end(map)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

def find_paths(maze, start, directions=directions):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited = {start:0}

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#'

    queue = deque([(start, 0)])

    while queue:
        (x, y), steps = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited[(nx, ny)] = steps + 1
            elif (nx, ny) in visited and visited[(nx, ny)] > steps + 1:
                queue.append(((nx, ny), steps + 1))
                visited[(nx, ny)] = steps + 1
    return visited

shortest_from_start = find_paths(map, start)
shortest_from_end = find_paths(map, end)

total = 0
original_shortest = shortest_from_start[end]

for (x1,y1), score1 in shortest_from_start.items():
    for (x2,y2), score2 in shortest_from_start.items():
        cut = abs(x1-x2) + abs(y1-y2)
        if cut <= 20:
            score = shortest_from_start[(x1,y1)] + shortest_from_end[(x2,y2)] + cut
            if original_shortest - score >= 100:
                total += 1
                
print("Day 20 part 1:",total)