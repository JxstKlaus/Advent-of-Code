example = [
    [2,4,1,3,4,3,2,3,1,1,3,2,3],
    [3,2,1,5,4,5,3,5,3,5,6,2,3],
    [3,2,5,5,2,4,5,6,5,4,2,5,4],
    [3,4,4,6,5,8,5,8,4,5,4,5,2],
    [4,5,4,6,6,5,7,8,6,7,5,3,6],
    [1,4,3,8,5,9,8,7,9,8,4,5,4],
    [4,4,5,7,8,7,6,9,8,7,7,6,6],
    [3,6,3,7,8,7,7,9,7,9,6,5,3],
    [4,6,5,4,9,6,7,9,8,6,8,8,7],
    [4,5,6,4,6,7,9,9,8,6,4,5,3],
    [1,2,2,4,6,8,6,8,6,5,5,6,3],
    [2,5,4,6,5,4,8,8,8,7,7,3,5],
    [4,3,2,2,6,7,4,6,5,5,5,3,3]
]

example = [
    [2,4,1,3],
    [20,40,10,3],
    [20,40,10,3],
    [2,4,1,3],
]

with open("2023\Day17\day17_input.txt", "r") as f:
    map = [list(map(int, str(line.strip()))) for line in f]
    

use_real_data = False
if not use_real_data:
    map = example

graph = {}


for x,line in enumerate(map):
    for y,num in enumerate(line):
        graph[(x,y)] = []
        if x-1 >= 0:
            graph[(x,y)].append((x-1,y))
        if x+1 <= len(map)-1:
            graph[(x,y)].append((x+1,y))
        if y-1 >= 0:
            graph[(x,y)].append((x,y-1))
        if y+1 <= len(map[0])-1:
            graph[(x,y)].append((x,y+1))

#for x in graph:
#    print(x, graph[x])

#    [2,4,1,3,4,3,2,3,1,1,3,2,3],
#    [3,2,1,5,4,5,3,5,3,5,6,2,3],
#    [3,2,5,5,2,4,5,6,5,4,2,5,4],
#    [3,4,4,6,5,8,5,8,4,5,4,5,2],
#    [4,5,4,6,6,5,7,8,6,7,5,3,6],
#    [1,4,3,8,5,9,8,7,9,8,4,5,4],
#    [4,4,5,7,8,7,6,9,8,7,7,6,6],
#    [3,6,3,7,8,7,7,9,7,9,6,5,3],
#    [4,6,5,4,9,6,7,9,8,6,8,8,7],
#    [4,5,6,4,6,7,9,9,8,6,4,5,3],
#    [1,2,2,4,6,8,6,8,6,5,5,6,3],
#    [2,5,4,6,5,4,8,8,8,7,7,3,5],
#    [4,3,2,2,6,7,4,6,5,5,5,3,3]

least_heat_loss = {(0,0):0}
for node in graph:
    curr_loss = least_heat_loss[node]
    if node not in least_heat_loss:
        least_heat_loss[node] = curr_loss
    for neighbor in graph[node]:
        if neighbor not in least_heat_loss:
            least_heat_loss[neighbor] = map[neighbor[0]][neighbor[1]] + curr_loss
        elif least_heat_loss[neighbor] > map[neighbor[0]][neighbor[1]] + curr_loss:
            least_heat_loss[neighbor] = map[neighbor[0]][neighbor[1]] + curr_loss
        

print(least_heat_loss[(len(map)-1, len(map[0])-1)])
for x in least_heat_loss:
    print(x, least_heat_loss[x])
#print(least_heat_loss)
