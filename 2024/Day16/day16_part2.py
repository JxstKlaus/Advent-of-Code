from collections import deque
example = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]
example = list(map(list, example))

with open("2024/Day16/day16_input.txt", "r") as f:
    maze = list(map(list, f.read().strip().split("\n")))

use_real_data = False
if not use_real_data:
    maze = example


def find_start_end(maze):
    start = None
    end = None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
    return start, end

start, end = find_start_end(maze)

def find_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    all_paths = []
    min_score = float('inf')

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#'

    queue = deque([(start, [start], 0, 0)])  # (current, path, score, last_direction)

    while queue:
        (x, y), path, score, last_dir = queue.popleft()
        
        if (x, y) == end:
            if score <= min_score:
                if score < min_score:
                    all_paths.clear()
                    min_score = score
                all_paths.append((path, score))
            continue

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in path:
                turn_cost = 1000 if last_dir != i else 0
                new_score = score + 1 + turn_cost
                queue.append(((nx, ny), path + [(nx, ny)], new_score, i))

    return all_paths


paths = find_paths(maze, start, end)

on_best_paths = set()
min_score = min(p[1] for p in paths)
for path, score in paths:
    if score == min_score:
        on_best_paths.update(path)

print("Day 16 part 2", len(on_best_paths))

