example = [
    [('R', 6), '#70c710)'],
    [('D', 5), '#0dc571)'],
    [('L', 2), '#5713f0)'],
    [('D', 2), '#d2c081)'],
    [('R', 2), '#59c680)'],
    [('D', 2), '#411b91)'],
    [('L', 5), '#8ceee2)'],
    [('U', 2), '#caa173)'],
    [('L', 1), '#1b58a2)'],
    [('U', 2), '#caa171)'],
    [('R', 2), '#7807d2)'],
    [('U', 3), '#a77fa3)'],
    [('L', 2), '#015232)'],
    [('U', 2), '#7a21e3)']
]

with open("2023\Day18\day18_input.txt", "r") as f:
    plan = [line.strip().split(" ") for line in f]
    plan = [[(x[0], int(x[1])), x[2][1:-1]] for x in plan]
    

use_real_data = True
if not use_real_data:
    plan = example


def updateMap(map,loc,dir,dist): # (x,y)
    x_cord = loc[0]
    y_cord = loc[1]
    new_map = []
    
    match dir:
        case "U":
            #expending map
            if x_cord - dist < 0:
                expansion = abs(x_cord - dist)
                #new_map = [["."] for x in range(len(map[0]))] * expansion + map
                new_map = [["." for x in range(len(map[0]))] for y in range(expansion)] + map
                map =  new_map
                x_cord += expansion
            
            #digging
            for x in range(x_cord,x_cord-dist-1,-1):
                map[x][y_cord] = "#"
            x_cord -= dist


        case "D":
            #expending map
            if x_cord + dist > len(map)-1:
                expansion = (x_cord + dist) - (len(map)-1)
                new_map = map + [["." for x in range(len(map[0]))] for y in range(expansion)]
                map = new_map
            
            #digging
            for x in range(x_cord,x_cord+dist+1):
                map[x][y_cord] = "#"
            x_cord += dist    

        case "R":
            #expending map
            if y_cord + dist > len(map[0]) - 1:
                expansion = (y_cord + dist) - (len(map[0])-1) 
                #new_map = [map[i] + ["."] * expansion for i,line in enumerate(map)]
                new_map = [map[i] + ["." for x in range(expansion)] for i,line in enumerate(map)]
                map = new_map
            
            #digging
            for y in range(y_cord,y_cord+dist+1):
                map[x_cord][y] = "#"
                

            y_cord += dist
        case "L":
            #expending map
            if y_cord - dist < 0:
                expansion = abs(y_cord - dist)
                new_map = [["."] * expansion + map[i] for i,line in enumerate(map)]
                map = new_map
                y_cord += expansion

            #digging
            for y in range(y_cord,y_cord-dist-1,-1):
                map[x_cord][y] = "#"
            y_cord -= dist
        

    return [map,(x_cord,y_cord)]
            


map = [["#"]]
loc = (0,0)

for i,((dir,dist),color) in enumerate(plan):
    map,loc = updateMap(map,loc,dir,dist)

        
def fillInside(map, x_pos, y_pos):
    queue = [(x_pos,y_pos)]
    while queue != []:
        for x,y in queue:
            if map[x][y] == ".":
                map[x][y] == "#"

            if map[x-1][y] == ".":
                map[x-1][y] = "#"
                queue.append((x-1,y))

            if map[x+1][y] == ".":
                map[x+1][y] = "#"
                queue.append((x+1,y))

            if map[x][y+1] == ".":
                map[x][y+1] = "#"
                queue.append((x,y+1))

            if map[x][y-1] == ".":
                map[x][y-1] = "#"
                queue.append((x,y-1))
            queue = queue[1::]
    return map

#finding a 100% valid inner cord
def validInnerCordFinder(map):
    for x,line in enumerate(map):
        for y in range(1,len(line)-1):
            if line[y-1] + line[y] + line[y+1] == ".#.":
                return (x+1,y+1)
            
in_cord = validInnerCordFinder(map)    

filled_map = fillInside(map,in_cord[0],in_cord[1])


print(f"Day 18 part 1 answer: {sum([line.count("#") for line in filled_map])}")


        
