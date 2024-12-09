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

safe_reports = 0

for report in reports:
    length = len(report)
    is_safe = True
    if report[0] > report[length-1]:
        is_increasing = False
    else:
        is_increasing = True
    
    for i in range(1,len(report)):
        diff = report[i-1]-report[i]

        if (is_increasing and (diff >= 0 or abs(diff) > 3)) or (not is_increasing and (diff <=0 or diff > 3)):
            is_safe = False
            break
            
    if is_safe:
        safe_reports += 1

print("Day 2 part 1 answer:", safe_reports)