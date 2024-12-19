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

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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

def find_lowest_scores(maze, start, dirs):
    queue = deque([(start, 0, dirs[0])])  # (current_position, score, previous_direction)
    visited = {}
    visited[start] = [0, dirs[0]]

    while queue:
        (x, y), score, prev_dir = queue.popleft()

        for dx, dy in dirs:
            new_pos = (x + dx, y + dy)
            new_dir = (dx, dy)

            new_score = score + 1
            if prev_dir and new_dir != prev_dir:
                new_score += 1000

            if new_pos not in visited and maze[new_pos[0]][new_pos[1]] != "#":
                queue.append((new_pos, new_score, new_dir))
                visited[new_pos] = [new_score, new_dir]
            elif new_pos in visited:
                if visited[new_pos][0] > new_score:
                    queue.append((new_pos, new_score, new_dir))
                    visited[new_pos] = [new_score, new_dir]
    return visited

visited = find_lowest_scores(maze, start, dirs)
print("Day 16 part 1", visited)

