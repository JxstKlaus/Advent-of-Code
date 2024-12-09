example = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]



with open("2024/Day2\day2_input.txt", "r") as f:
    reports = [list(map(int, x.strip().split(" "))) for x in f]

use_real_data = True
if not use_real_data:
    reports = example

def check_if_not_safe(num1,num2):
    diff = abs(num1-num2)
    return diff < 1 or diff > 3

def is_safe_report(report):
    is_increasing = is_increasing_sequence(report)
    is_decreasing = is_decreasing_sequence(report)

    if not is_increasing and not is_decreasing:
        return False
    
    for i in range(len(report) - 1):
        if check_if_not_safe(report[i+1], report[i]):
            return False

    return True


def is_increasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

def is_decreasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            return False
    return True

safe_reports = 0
for report in reports:
    ints = list(map(int, report))
    if is_safe_report(ints):
        safe_reports += 1
        continue

    valid_with_dampener = False

    for i in range(len(ints)):
        modified_report = [x for j, x in enumerate(ints) if j != i]
        if is_safe_report(modified_report):
            valid_with_dampener = True
            break

    if valid_with_dampener:
        safe_reports += 1


print("Day 2 part 2 answer:", safe_reports)

#279 too low
#308