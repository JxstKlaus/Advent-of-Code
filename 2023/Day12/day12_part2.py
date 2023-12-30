example = [
    ["???.###", (1,1,3)],
    [".??..??...?##.", (1,1,3)],
    ["?#?#?#?#?#?#?#?", (1,3,1,6)],
    ["????.#...#...", (4,1,1)],
    ["????.######..#####.", (1,6,5)],
    ["?###????????", (3,2,1)]
]

with open("Day12\day12_input.txt", "r") as f:
    springs_data = [line.strip().split(" ") for line in f]
    springs_data = [[line[0],tuple([int(x) for x in line[1].split(",")])] for line in springs_data]


use_real_data = True
if not use_real_data:
    springs_data = example


#optimizing the already existing function with cache
#a.k.a storing the already calculated outcomest to not waste processing power with calculating duplicates
cache = {}
def possibleCase(springs,nums):
    if springs == "":
        if nums != ():
            return 0
        else:
            return 1

    if nums == ():
        if "#" in springs:
            return 0
        else:
            return 1
    
    key = (springs,nums)
    if key in cache:
        return cache[key]

    count = 0

    if springs[0] in ".?": #    ? = .
        count += possibleCase(springs[1:],nums)

    if springs[0] in "#?": #    ? = # -->  start of a new block
        if len(springs) >= nums[0] and "." not in springs[:nums[0]] and (len(springs) == nums[0] or springs[nums[0]] != "#"):
            count += possibleCase(springs[nums[0]+1:], nums[1:])
    
    cache[key] = count
    return count

total = 0
#c = 0
for springs,nums in springs_data:
    #c += 1
    #if c % 50 ==0: print(c)
    nums = nums * 5
    springs = "?".join([springs]*5)
    total += possibleCase(springs,nums)
print(f"Part 1 answer: {total}")

