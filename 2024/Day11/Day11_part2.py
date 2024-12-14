example = {125:1, 17:1}

with open("2024/Day11/day11_input.txt", "r") as f:
    temp = list(map(int, f.read().strip().split(" ")))
    stones = {}
    for stone in temp:
        if stone in stones:
            stones[stone] += 1
        else:
            stones[stone] = 1 

use_real_data = True
if not use_real_data:
    stones = example

for _ in range(75):
    new_stones = {}
    for stone in stones:
        str_stone = str(stone)
        digit_len = len(str_stone)
        if stone == 0:
            if 1 not in new_stones:
                new_stones[1] = 0
            new_stones[1] += stones[stone]

        elif digit_len % 2 == 0:
            mid = digit_len // 2
            s1 = (int(str_stone[:mid]))
            s2 = (int(str_stone[mid:]))
            if s1 not in new_stones:
                new_stones[s1] = 0
            if s2 not in new_stones:
                new_stones[s2] = 0
            new_stones[s1] += stones[stone]
            new_stones[s2] += stones[stone]
        else:
            s = stone * 2024
            if s not in new_stones:
                new_stones[s] = 0
            new_stones[s] += stones[stone]
    stones = new_stones

print("Day 11 part 2: ", sum([stones[x] for x in stones]))