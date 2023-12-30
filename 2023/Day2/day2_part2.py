with open("Day2\day2_input.txt", "r") as f:
    file = []
    for line in f:
        line = line.strip().split(": ")
        line[1] = line[1].replace(";", ",")
        line[1] = line[1].split(", ")
        file.append(line)

#['Game 2', ['1 green', '17 red', '1 blue', '6 red', '7 green', '2 blue', '4 red', '7 green', '1 green', '6 red', '2 blue']]

print(file[0])
min_cubes =  {"red": 0,
              "green": 0,
              "blue": 0,}

sum_power = 0

for game_id in file:
    min_cubes["red"] = min_cubes["green"] = min_cubes["blue"] = 0

    #finding the max of each color

    for cube in game_id[1]:
        cube_split = cube.split(" ")
        if int(cube_split[0]) > min_cubes[cube_split[1]]:
            min_cubes[cube_split[1]] = int(cube_split[0])
    
    #multiplying the colors together
    sub_set = 1
    for min in min_cubes:
        sub_set *= min_cubes[min]

    #adding the multiplycated number to the sum
    sum_power += sub_set

        
print(f"Day 2 part 2 answer: {sum_power}")

