example_data = [
    [123, 328,  51, 64],
    [45, 64,  387, 23],
    [6, 98,  215, 314],
    ["*", "+",  "*", "+" ]
]

with open("2025/Day6/day6_input.txt", "r") as f:
    rows = [line.split() for line in f]

numbers = [list(map(int, row)) for row in rows[:-1]]
operators = rows[-1]

use_real_data = True
if not use_real_data:
    numbers, operators = example_data[:-1], example_data[-1]

total = 0
for col in range(len(numbers[0])):
    if operators[col] == "*":
        result = 1
    elif operators[col] == "+":
        result = 0

    for row in range(len(numbers)):
        if operators[col] == "*":
            result *= numbers[row][col]
        elif operators[col] == "+":
            result += numbers[row][col]

    total += result
    

print(total)