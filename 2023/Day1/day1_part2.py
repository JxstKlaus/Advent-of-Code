document = [line.strip() for line in open("Day1\day1_input.txt", "r")]

dictionary = {"one" : 1,
              "two" : 2,
              "three" : 3,
              "four" : 4,
              "five" : 5,
              "six" : 6,
              "seven" : 7,
              "eight" : 8,
              "nine" : 9
              }

temp_string = ""
line_string = ""
new_document = []
for line in document: 

    
    line_string = ""
    for digit in line:
        if digit.isdigit():
            line_string += digit
            temp_string = ""
        else:
            temp_string += digit
            for number in dictionary:
                if number in temp_string:
                    line_string += str(dictionary[number])
                    temp_string = ""
                    break
    new_document.append(line_string)

print(new_document[0:12])

print(f"Day 1 part 2 answer: {sum(int(x[0] + x[-1]) for x in new_document)}")
