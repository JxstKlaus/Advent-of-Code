example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

with open("2024/Day4/day4_input.txt", "r") as f:
    table = [x.strip() for x in f]

use_real_data = True
if not use_real_data:
    table = example

#lines are 3 long string
def is_mas_found(line1, line2, line3):
    if line2[1] == "A":
        if line1[0] == line1[2] == "M" and line3[0] == line3[2] == "S":
            return True
        elif line3[0] == line3[2] == "M" and line1[0] == line1[2] == "S":
            return True
        elif line1[0] == line3[0] == "M" and line1[2] == line3[2] == "S":
            return True
        elif line1[2] == line3[2] == "M" and line1[0] == line3[0] == "S":
            return True

xmas_count = 0
for i in range(len(table)-2):
    for j in range(len(table[0])-2):
        if is_mas_found(table[i][j:j+3], table[i+1][j:j+3], table[i+2][j:j+3]):
            xmas_count += 1

print("Day 4 part 2:", xmas_count)