example = "2333133121414131402"
#example = "1313165"
example = list(map(int, example))

with open("2024/Day9/day9_input.txt", "r") as f:
    map = list(map(int, f.read().strip()))

use_real_data = True
if not use_real_data:
    map = example

rearranged_map = []
length = 0
for i in range(len(map)):
    if i%2 == 0:
        rearranged_map.extend(map[i] * [i//2])
    elif map[i] != 0:
        rearranged_map.extend(map[i] * [-1])
    length += map[i]

j_s = j_e = len(rearranged_map)-1
while j_s > 0:
    #finding the whole file 
    if rearranged_map[j_e] != -1:
        while True:
            j_s -= 1
            if rearranged_map[j_s] == -1 or rearranged_map[j_s] != rearranged_map[j_e]: 
                break
        disk_part = [j_s+1, j_e]
        length = j_e-j_s

        #found! Searching for empty space
        i_s = None
        i_e = None
        empty_part = []
        for i in range(len(rearranged_map[:j_s+2])): # +2 has to added beacause if the sequence ends with -1 then for cycle ends without updating empty part 
            if rearranged_map[i] == -1 and i_s == None:
                i_s = i
                i_e = i
            elif i_s != None and rearranged_map[i] == -1:
                i_e += 1
            elif i_s != None and rearranged_map[i] != -1:
                if length <= i_e-i_s+1:
                    empty_part = [i_s, i_e]
                    break
                i_s = None
                i_e = None

        #moving file if big enough space found
        if empty_part != []:
            for i in range(length):
                rearranged_map[disk_part[0]+i], rearranged_map[empty_part[0]+i] = rearranged_map[empty_part[0]+i], rearranged_map[disk_part[0]+i]

        j_e = j_s
    else:
        j_e -= 1
        j_s = j_e

print("Day9 part 2:", sum(i*rearranged_map[i] for i in range(len(rearranged_map)) if rearranged_map[i] != -1))