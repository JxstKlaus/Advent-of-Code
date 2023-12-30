with open("Day6\day6_input.txt", "r") as f:
    data = []
    for line in f:
        data.append([x for x in line.strip().split(":")[1].split()])         


example = (['7','15','30'],['9','40','200'])

use_real_input = True
if not use_real_input:
    data = example

input = (int("".join(data[0])), int("".join(data[1])))
print(input)

chances_to_win = 0


time_1 = input[0]//2+1
time_2 = input[0]//2

if input[0] % 2 == 0:
    chances_to_win +=1

for half_time in range(input[0]//2):

    if time_1*(input[0] - time_1) > input[1]:
        chances_to_win += 1
    else:
         break
    if time_2*(input[0] - time_2) > input[1]:
        chances_to_win += 1
    else:
         break
    time_1 += 1
    time_2 -= 1

print(f"Answer to part 2: {chances_to_win}")


