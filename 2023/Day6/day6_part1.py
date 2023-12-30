with open("Day6\day6_input.txt", "r") as f:
    data = []
    for line in f:
        data.append([int(x) for x in line.strip().split(":")[1].split()])      


example = [[7,15,30],[9,40,200]]

use_real_input = True
if not use_real_input:
    data = example

input = []
for time,dist in zip(data[0],data[1]):
    input.append((time,dist))


chances_to_win = 1
for total_time,dist in input:
    race_wins = 0
    for press_time in range(total_time):
        if press_time*(total_time - press_time) > dist:
            race_wins += 1
    chances_to_win *= race_wins
print(f"Answer to part 1: {chances_to_win}")

