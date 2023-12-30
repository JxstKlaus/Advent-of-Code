with open("Day2\day2_input.txt", "r") as f:
    file = []
    for line in f:
        line = line.strip().split(": ")
        line[1] = line[1].replace(";", ",")
        line[1] = line[1].split(", ")
        file.append(line)
#['Game 2', ['1 green', '17 red', '1 blue', '6 red', '7 green', '2 blue', '4 red', '7 green', '1 green', '6 red', '2 blue']]
print(file[0])
all_cubes =  {"red": 12,
              "green": 13,
              "blue": 14,}

sum_id = 0

for game_id in file:
    impossible = False
    for cube in game_id[1]:
        cube_split = cube.split(" ")
        if int(cube_split[0]) > all_cubes[cube_split[1]]:
            impossible = True
            break
    
    if impossible==False:
        sum_id += int(game_id[0].split(" ")[1])
        
print(f"Day 2 part 1 answer: {sum_id}")



