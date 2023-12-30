document = [line.strip() for line in open("Day1\day1_input.txt", "r")]

total_sum = 0
digit = ""
for line in document:
    digit = ""
    for first in line:
        if first.isdigit():
            digit += first
            break
    for last in line[::-1]:
        if last.isdigit():
            digit += last
            break
    total_sum += int(digit)

print(f"Day 1 part 1 answer: {total_sum}")