example_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("2025/Day2/day2_input.txt", "r") as f:
    ranges = f.readline()

use_real_data = True
if not use_real_data:
    ranges = example_data

def from_list_to_int(digits):
    number = 0
    for d in digits:
        number = number * 10 + int(d)
    print(number)

range_list = [tuple(map(int, x.split("-"))) for x in ranges.split(",")]

results = set()
for start,end in range_list:
    start_len = len(str(start))
    end_len = len(str(end))
    
    for length in range(start_len, end_len + 1):
        for pattern_len in range(1, length // 2 + 1):
            if length % pattern_len == 0:

                # Part 1: fixed repeat count to 2
                #repeat_count = 2

                # Part 2: variable repeat count
                repeat_count = length // pattern_len

                for pattern in range(10**(pattern_len-1), 10**pattern_len):
                    number = int(str(pattern) * repeat_count)
                    if start <= number <= end:
                        results.add(number)
print(sum(results))