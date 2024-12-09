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

def rotate_90deg(strings):
    rotated = list(zip(*strings))
    return [''.join(row) for row in rotated]

def get_diagonals(strings):
    n = len(strings)
    m = len(strings[0]) if strings else 0
    
    # Collect diagonals from top-left to bottom-right (\)
    diagonals = []
    for d in range(n + m - 1):
        diag1 = []
        diag2 = []
        for i in range(n):
            j1 = d - i  # Index for top-left to bottom-right
            j2 = i - (d - n + 1)  # Index for top-right to bottom-left
            
            if 0 <= j1 < m:
                diag1.append(strings[i][j1])
            if 0 <= j2 < m and 0 <= d - i < n:
                diag2.append(strings[i][j2])

        if diag1:
            diagonals.append("".join(diag1))
        if diag2:
            diagonals.append("".join(diag2))
    
    return diagonals


xmas_count = 0
rotated_table = rotate_90deg(table)

#counting horizontally and vertically 
for row, col in zip(table, rotated_table):
    lines = [row, col]
    for line in lines:
        xmas_count += (line.count("XMAS") + line.count("SAMX"))

#counting diagonally
for line in get_diagonals(table):
    xmas_count += (line.count("XMAS") + line.count("SAMX"))
print("Day 4 part 1:",  xmas_count)