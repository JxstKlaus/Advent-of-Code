example = [
["#.##..##.",
"..#.##.#.",
"##......#",
"##......#",
"..#.##.#.",
"..##..##.",
"#.#.##.#."],

["#...##..#",
"#....#..#",
"..##..###",
"#####.##.",
"#####.##.",
"..##..###",
"#....#..#"]
]

with open("Day13\day13_input.txt", "r") as f:
    data = [line.strip() for line in f]
    patterns = []
    temp = []
    for i,line in enumerate(data):
        if line == "" or i == len(data)-1:
            patterns.append(temp)
            temp = []
        else:
            temp.append(line)

use_real_data = True
if not use_real_data:
    patterns = example


def rotatePattern(pattern):
    return ["".join([pattern[y][x] for y in range(len(pattern))][::-1]) for x in range(len(pattern[0]))]

def horiRefl(pattern):
    top_index = None
    bottom_index = None
    pairs = []
    for i in range(len(pattern)-1):
        top_index = i
        bottom_index = i+1   
        if pattern[i] == pattern[i+1]:
            pairs.append((top_index,bottom_index,0))
        else:
            error = 0
            for char1,char2 in zip(pattern[i],pattern[i+1]):
                if char1 != char2:
                    error += 1
                if error > 1:
                    break
            if error == 1:
                pairs.append((top_index,bottom_index))
        
    for pair in pairs:
        top_index = pair[0]
        bottom_index = pair[1]
        error = 0
        result = bottom_index

        for t_line,b_line in zip(pattern[0:bottom_index][::-1],pattern[bottom_index:len(pattern)]):
            if t_line != b_line:
                for char1,char2 in zip(t_line,b_line):
                    if char1 != char2:
                        error += 1
            if error > 1:
                break

            if (top_index == 0 or bottom_index == len(pattern)-1) and error == 1:
                return result

            top_index -= 1
            bottom_index += 1

    return 0

    
def vertRefl(pattern):
    return horiRefl(rotatePattern(pattern))


total = 0
for pattern in patterns:
    total += horiRefl(pattern)*100 + vertRefl(pattern)
print(f"Part 2 answer: {total}")




    