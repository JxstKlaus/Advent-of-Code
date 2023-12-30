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


seeds = [(seeds[x],seeds[x]+seeds[x+1]) for x in range(0,len(seeds),2)]



for map in input:
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for a,b,c in map:           #a = destination start, b = source start, c = range
            overlap_start = max(start,b)
            overlap_end = min(end, b+c)
            if overlap_start < overlap_end:
                new.append((overlap_start - b + a, overlap_end - b +a))
                if overlap_start > start:
                    seeds.append((start,overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end,end))
                break
        else:
            new.append((start,end))
    seeds = new

print(min(seeds)[0])

 # 47909639
