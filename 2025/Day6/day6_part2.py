example_data = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  ",
]

with open("2025/Day6/day6_input.txt", "r") as f:
    rows = [line.strip("\n") for line in f.readlines()]

numbers = rows[:-1]
operators = rows[-1]

use_real_data = True
if not use_real_data:
    numbers, operators = example_data[:-1], example_data[-1]

num_strings = []
total = 0
for col in range(len(numbers[0])-1, -1, -1):
    num_string = ""
    for row in range(len(numbers)):
        char = numbers[row][col]
        if char != " ":
            num_string += char
        
    if num_string:
        num_strings.append(int(num_string))


    if operators[col] == "*":
        result = 1
        for num in num_strings:
            result *= num
        num_strings = []
        total += result

    elif operators[col] == "+":
        result = sum(num_strings)
        num_strings = []
        total += result

print(total)