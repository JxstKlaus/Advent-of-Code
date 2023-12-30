example = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

with open("Day3\day_3_input.txt", "r") as f:
    data = []
    for line in f:
        data.append(line.strip())



use_input = True
if use_input == False:
    data = example

#finding all the nummbers line by line

all_numbers = []
all_gears = []
num = ""

for row_index,line in enumerate(data):
    line_numbers = []
    line_gears = []
    line = line + "."

    for column_index,char in enumerate(line):
        if char.isdigit():
            if num =="":
                start = column_index
            num += char

        elif char == "*":
            line_gears.append(column_index)
            if num != "":
                end = start + len(num)-1
                line_numbers.append([start,end])
                num = ""

        elif not char.isdigit() and num != "":
            #start = line.index(num)
            #print(line,num)
            end = start + len(num)-1
            line_numbers.append([start,end])
            num = ""
        
        


    all_gears.append(line_gears)
    all_numbers.append(line_numbers)




def lineExtractor(data,index):
    #dealing with out of range 
    if index == 0:
        lines = ["",data[index],data[index+1]]
    elif index == len(data)-1:
        lines = [data[index-1], data[index], ""]
    else:
        lines = data[index-1:index+2]
    return lines



sum1 = 0
sum2 = 0
for row_index,gears in enumerate(all_gears): # gears =[3,4,6,55]
    surround_rows = lineExtractor(all_numbers,row_index)
    #print(surround_rows)
    for column_index, gear in enumerate(gears): # gear = 4
        cords_in_range = []
        for cord_row in surround_rows:
            for cord in cord_row:
                if abs(gear-cord[0]) <= 1 or  abs(gear-cord[1]) <= 1:
                    cords_in_range.append([all_numbers.index(cord_row),cord])
        
        if len(cords_in_range) == 2:
            #print(cords_in_range)
            power = 1
            for cord in cords_in_range:
                power *= int(data[cord[0]][cord[1][0]:cord[1][1]+1])
            sum2 += power


        if len(cords_in_range) > 0:
            #print(cords_in_range)
            for cord in cords_in_range:
                sum1 += int(data[cord[0]][cord[1][0]:cord[1][1]+1])
            



print(f"Answer to Day 3 Part 1 {sum1}")    
print(f"Answer to Day 3 Part 2 {sum2}")

#527364
#79026871