example = [
    '1,0,1~1,2,1',
    '0,0,2~2,0,2',
    '0,2,3~2,2,3',
    '0,0,4~0,2,4',
    '2,0,5~2,2,5',
    '0,1,6~2,1,6',
    '1,1,8~1,1,9'
]

with open("2023\Day22\day22_input.txt", "r") as f:
    data = [line.strip() for line in f]

use_real_data = False
if not use_real_data:
    data = example

brick_cords = [[list(map(int,start.split(","))),list(map(int,end.split(",")))] for start,end in [line.split("~") for line in data]]

#sorting bricks by the z cord
#if the brick extends on the z axis always the starting value gets the lower num
brick_cords.sort(key=lambda x:x[0][2])

#settleing the bricks
for i,cord in enumerate(brick_cords):
    for other in brick_cords:
        if ((other[0][0] and other[1][0]) not in range(cord[0][0],cord[1][0]+1) and (other[0][1] and other[1][1]) not in range(cord[0][1],cord[1][1]+1)):
            diff = brick_cords[i][1][2] - brick_cords[i][0][2]
            brick_cords[i][0][2] = other[1][2]
            brick_cords[i][1][2] = brick_cords[i][0][2] + diff


for x in brick_cords:
    print(x)


brick_cords.sort(key=lambda x:x[0][2])
def supportCheck(start,end,curr_index,brick_cords):
    supported = []
    for brick in brick_cords[curr_index::]:
        if brick[0][2] > end[2]+1:
            break
    
        if end[2]+1 == brick[0][2] and ((brick[0][0] or brick[1][0]) in range(start[0],end[0]+1) or (brick[0][1] or brick[1][1]) in range(start[1],end[1]+1)):
            supported.append(brick)
    return supported

#B -> [0,0,2],[2,0,2]
print(supportCheck([1,0,1],[1,2,1],1,brick_cords))

print((2 and 2) in range(0,0))
print((0 and 2) in range(0,2))