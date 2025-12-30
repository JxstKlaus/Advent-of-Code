example_data = [
    (7,1),
    (11,1),
    (11,7),
    (9,7),
    (9,5),
    (2,5),
    (2,3),
    (7,3)
]

with open("2025/Day9/day9_input.txt", "r") as f:
    tiles = [tuple(map(int, line.strip().split(","))) for line in f]

use_real_data = True
if not use_real_data:
    tiles = example_data

def get_area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)

edges = [(i,j) for i in range(len(tiles)) for j in range(i+1, len(tiles))]
edges.sort(key=lambda x: get_area(tiles[x[0]], tiles[x[1]]), reverse=True)

print(get_area(tiles[edges[0][0]], tiles[edges[0][1]]))