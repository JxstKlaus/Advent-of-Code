
example = [
    'seeds: 79 14 55 13',

    'seed-to-soil map:',
    '50 98 2', #50-100
    '52 50 48', # 52-98

    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',

    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',

    'water-to-light map:',
    '88 18 7',
    '18 25 70',

    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',

    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',

    'humidity-to-location map:',
    '60 56 37',
    '56 93 4',
]

with open("Day5\day5_input.txt", "r") as f:
    data = []
    for line in f:
        if line != '\n':
            data.append(line.strip())

use_input = True
if use_input == False:
    data = example

seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]     #separating the seeds


#removing text and only leaving the maps 

input = []
maps = []
for line in data[1:]:
    if data.index(line) == len(data) -1:
        input.append(maps)
        

    elif line[0].isdigit():
        line = line.split(" ")
        line = [int(x) for x in line]
        maps.append(line)

    elif maps != []:
        input.append(maps)
        maps = []



def rangeChecker(map, start, range): #map = [  [],  [],  [], ...]
    ranges = []
    end = range + start
    for line in map:
        #ranges.append([line[1], line[1]+line[2]])
        if start >= line[0] and end <= line[1]:
            ranges.append(line)
    return ranges
    #return min(bottom_ranges), max(top_ranges)

ranges =rangeChecker(input[0],3037945983, 743948277)










#converting seed to the location
def converter(maps,seed):    #map = [  [],  [],  [], ...] seed = 79
    for map in maps:
        for line in map:
            if line[1] <= seed <= line[1] + line[2]:
                return line[0] + (seed-line[1])  
    return seed
"""
def converter(map,seed):    #map = [  [],  [],  [], ...] seed = 79

    for line in map:
        out_of_range = 0
        if line[1] <= seed <= line[1] + line[2]:
            return line[0] + (seed-line[1])  
        else:
            out_of_range += 1
        if out_of_range == len(line):
            return False
    return seed
"""

locations = []
lowest_location  = 9999999999


for i in range(0,len(seeds)-1,2):
    seed = seeds[i]
    range_  = seeds[i+1]
    #print(seed,range_)
    for j in range(range_):
        for maps in input: 
            seed = converter(maps, seed)
        if seed < lowest_location:
            lowest_location = seed
        #locations.append(seed)
        seed = seeds[i] + j
    print(f"{i}")

 
print(f"Answer to part 2: {lowest_location}")
        
        
            
   
# 343272167 too high
