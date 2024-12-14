example = [125, 17]

with open("2024/Day11/day11_input.txt", "r") as f:
    stones = list(map(int, f.read().strip().split(" ")))

use_real_data = True
if not use_real_data:
    stones = example


for _ in range(25):
    new_stones = []
    for i,stone in enumerate(stones):
        str_stone = str(stone)
        digit_len = len(str_stone)
        if stone == 0:
            new_stones.append(1)
        elif digit_len % 2 == 0:
            mid = digit_len // 2
            new_stones.append(int(str_stone[:mid]))
            new_stones.append(int(str_stone[mid:]))
        else:
            new_stones.append(stone * 2024)
        stones = new_stones
print("Day 11 part 1: ",len(stones))