from collections import deque

example_data = [
    (5,4),(4,2),(4,5),(3,0),(2,1),(6,3),(2,4),(1,5),(0,6),(3,3),(2,6),(5,1),(1,2),(5,5),(2,5),(6,5),(1,4),(0,4),(6,4),(1,1),(6,1),(1,0),(0,5),(1,6),(2,0)
]

WIDTH = 70
HEIGHT = 70

with open("2024/Day18/day18_input.txt", "r") as f:
    corrupted = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in f]

use_real_data = True
if not use_real_data:
    corrupted = example_data
    WIDTH = 6
    HEIGHT = 6

end = (HEIGHT, WIDTH)

def find_path(corrupted, rows=HEIGHT+1, cols=WIDTH+1, end=end):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0,0)
    queue = deque([start])
    visited = set()

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while queue:
        (x,y) = queue.pop()
        visited.add((x,y))
        if (x, y) == end:
            return True
        for dx, dy in dirs:
            new_pos = (x + dx, y + dy)

            if new_pos not in visited and new_pos not in corrupted and is_in_bounds(new_pos[0], new_pos[1]):
                queue.append(new_pos)
    return False



min = 0
max = len(corrupted)
while max - min > 1:
    if find_path(corrupted[:min]):
        previous_min = min
        min += (max - min) // 2
    else:
        max = min
        min = previous_min 
    
print("Day 18 part 2:", corrupted[min])

