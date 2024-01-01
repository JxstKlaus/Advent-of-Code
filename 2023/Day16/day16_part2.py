#example:

#   .|...\....
#   |.-.\.....
#   .....|-...
#   ........|.
#   ..........
#   .........\
#   ..../.\\..
#   .-.-/..|..
#   .|....-|.\
#   ..//.|....

use_real_data = True

file = 'day16_input.txt'
if not use_real_data:
    file = "example.txt"
    
with open(f"2023\Day16\{file}", "r") as f:
    tiles = [line.strip() for line in f]


def resetEnergizedTiles():
    energized_tiles = []
    for x in range(len(tiles)):
        row = []
        for y in range (len(tiles[0])):
            row.append(".")
        energized_tiles.append(row)
    return energized_tiles
  

def beamDirection(beam,tile):
    match tile:
        case "/":
            if beam[1] == 1:
                return [(-1,0)]
            elif beam[1] == -1:
                return [(1,0)]
            elif beam[0] == 1:
                return [(0,-1)]
            elif beam[0] == -1:
                return [(0,1)]
            
        case "\\":
            if beam[1] == 1:
                return [(1,0)]
            elif beam[1] == -1:
                return [(-1,0)]
            elif beam[0] == 1:
                return [(0,1)]
            elif beam[0] == -1:
                return [(0,-1)]
            
        case "|":
            if beam in [(0,1), (0,-1)]:
                return [(1,0), (-1,0)]

        case "-":
            if beam in [(1,0), (-1,0)]:
                return [(0,1), (0,-1)]
    return [beam]

#def rotateTiles(pattern):
#    return ["".join([pattern[y][x] for y in range(len(pattern))][::-1]) for x in range(len(pattern[0]))]

start_beams = []
for x in range(len(tiles)):
    start_beams.append([(x,0), (0,1)])
    y = len(tiles[0]) - 1
    start_beams.append([(x,y), (0,-1)])

for y in range(len(tiles[0])):
    start_beams.append([(0,y), (1,0)])
    x = len(tiles) - 1
    start_beams.append([(x,y), (-1,0)])


#beams = [[(0,0),(0,1)]] # [curr_pos, beam_dir]


results = []
cycle = 0
for start_beam in start_beams:

    cycle += 1
    if cycle % 20 == 0:
        print(cycle)

    energized_tiles = resetEnergizedTiles()
    beams = [start_beam]
    cache = []
    while beams != []:
        for beam in beams:
            if beam in cache:
                beams = beams[1::]
            else:
                beam_pos = beam[0]
                beam_dir = beam[1]
                
                if len(tiles)-1 < beam_pos[0] or beam_pos[0] < 0 or len(tiles[0])-1 < beam_pos[1] or beam_pos[1] < 0:
                    beams = beams[1::]
                else:
                    tile = tiles[beam_pos[0]][beam_pos[1]]

                    energized_tiles[beam_pos[0]][beam_pos[1]] = "#"
                    new_beam_dir = beamDirection(beam_dir,tile)
                    
                    for dir in new_beam_dir:
                        new_beam = [(beam_pos[0] + dir[0], beam_pos[1] + dir[1]) , dir]
                        if new_beam not in beams:
                            beams.append(new_beam)
                        else:
                            beams.remove(new_beam)
                cache.append(beam)

    results.append(sum([line.count("#") for line in energized_tiles]))

print(f"Part 2 answer: {max(results)}")
        