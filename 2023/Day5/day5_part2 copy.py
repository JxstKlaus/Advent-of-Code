
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

def SeedToLoc(input,seed):    #maps = [  [],  [],  [], ...] seed = 79
    for maps in input:
        for map in maps:
            
            if map[1] <= seed <= map[1] + map[2]: # [dest_start, source_start, range]
                seed = map[0] + (seed-map[1])
            
        return seed

   




ranges = [[seeds[x],seeds[x]+seeds[x+1]] for x in range(0,len(seeds),2)]

    
cut_ranges = [ranges[1]]
for seed_range in ranges:   #seed_range = [start,end]
    for index in range(len(cut_ranges)):
        
        start_cut = cut_ranges[index][0]
        end_cut = cut_ranges[index][1]
        #print(start_cut,end_cut)

        if (start_cut and end_cut) in range(seed_range[0],seed_range[1]+1):
            cut_ranges[index][0] = start_cut- (start_cut - seed_range[0])
            cut_ranges[index][1] = end_cut + (seed_range[1]-end_cut)

            break
            
            

        elif start_cut in range(seed_range[0],seed_range[1]+1):
            cut_ranges[index][0] = start_cut- (start_cut - seed_range[0])

            break
            
            

        elif end_cut in range(seed_range[0],seed_range[1]+1):
            cut_ranges[index][1] = end_cut + (seed_range[1] - end_cut)

            break
            
        
        else:
            cut_ranges.append(seed_range)
            break

        
print(f"Cut {cut_ranges}")
print(ranges)


print((42 and 80) in range(10,34))



total_operations = 0
for seed_range in ranges:
    total_operations += seed_range[1]-seed_range[0]
print(total_operations)


total_operations = 0
for seed_range in cut_ranges:
    total_operations += seed_range[1]-seed_range[0]
print(total_operations)

    

    
            
   
# 343272167 too high
