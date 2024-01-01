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

use_real_data = False

file = 'day16_input.txt'
if not use_real_data:
    file = "example.txt"
    
with open(f"2023\Day16\{file}", "r") as f:
    tiles = [line.strip() for line in f]


energized_tiles = [["."] * len(tiles[0])] * len(tiles)
energized_tiles = []
for x in range(len(tiles)):
    row = []
    for y in range (len(tiles[0])):
        row.append(".")
    energized_tiles.append(row)
  

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



beams = [[(0,0),(0,1)]] # [curr_pos, beam_dir]
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

print(f"Part 1 answer: {sum([line.count("#") for line in energized_tiles])}")




        