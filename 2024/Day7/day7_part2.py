example = [
    [190, [10, 19]],
    [3267, [81, 40, 27]],
    [83, [17, 5]],
    [156, [15, 6]],
    [7290, [6, 8, 6, 15]],
    [161011, [16, 10, 13]],
    [192, [17, 8, 14]],
    [21037, [9, 7, 18, 13]],
    [292, [11, 6, 16, 20]]
]

with open("2024/Day7/day7_input.txt", "r") as f:
    equations = [[int(eq[0]), list(map(int, eq[1].split(" ")))] for eq in [x.strip().split(": ") for x in f]]

use_real_data = True
if not use_real_data:
    equations = example


def is_valid(target,nums):
    outcomes = [nums[0]]
    final = set()
    for i,num in enumerate(nums[1:]):
        new_outcomes = []
        for outcome in outcomes:
            c1 = num + outcome
            c2 = num * outcome
            c3 = int(str(outcome) + str(num))

            if i == len(nums)-2:
                final.add(c1)
                final.add(c2)
                final.add(c3)
            else:
                new_outcomes.append(c1)
                new_outcomes.append(c2)
                new_outcomes.append(c3)
        outcomes = new_outcomes
    return target in final


total = 0
for value, numbers in equations:
    if is_valid(value, numbers):
        total += value

print("Day 7 part 2: ",total)