example_data = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]
with open("2025/Day3/day3_input.txt", "r") as f:
    batteries = [line.strip() for line in f.readlines()]

use_real_data = True
if not use_real_data:
    batteries = example_data

batteries = [[int(char) for char in line] for line in batteries]


# Part 1
#length = 2

# Part 2
length = 12

ratings = []
for battery in batteries:
    result = []
    start = 0

    for i in range(length):
        # leave (n - i - 1) digits after the choice
        end = len(battery) - (length - i - 1)
        
        # Choose the max digit in the allowed range
        max_digit = max(battery[start:end])
        max_index = battery.index(max_digit, start, end)

        result.append(str(max_digit))
        start = max_index + 1

    ratings.append(int("".join(result)))

print(sum(ratings))