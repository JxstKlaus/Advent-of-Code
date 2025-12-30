example_data = [
    [162,817,812],
    [57,618,57],
    [906,360,560],
    [592,479,940],
    [352,342,300],
    [466,668,158],
    [542,29,236],
    [431,825,988],
    [739,650,466],
    [52,470,668],
    [216,146,977],
    [819,987,18],
    [117,168,530],
    [805,96,715],
    [346,949,466],
    [970,615,88],
    [941,993,340],
    [862,61,35],
    [984,92,344],
    [425,690,689]
]

with open("2025/Day8/day8_input.txt", "r") as f:
    junctions = [list(map(int, line.strip().split(","))) for line in f]

n = 1000

use_real_data = True
if not use_real_data:
    junctions = example_data
    n = 10

def get_euclidian_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5

edges = [(i,j) for i in range(len(junctions)) for j in range(i+1, len(junctions))]
edges.sort(key=lambda x: get_euclidian_distance(junctions[x[0]], junctions[x[1]]))

parent = [i for i in range(len(junctions))]

def root(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    x = root(i)
    y = root(j)
    parent[x] = y

circuits = len(junctions)


solution = 0
for i,j in edges:
    if root(i) == root(j): continue
    union(i, j)
    circuits -= 1
    if circuits == 1:
        solution = junctions[i][0] * junctions[j][0]
        break
    
print(solution)