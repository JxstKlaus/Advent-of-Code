

example = [
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

with open("Day4\day4_input.txt", "r") as f:
    data = []
    for line in f:
        data.append(line.strip())



use_input = True
if use_input == False:
    data = example

data = [x.split(": ")[1].split(" | ") for x in data]
data = [[[int(num) for num in list.split(" ") if num.isdigit()] for list in line] for line in data]


#checks the number of matches on a card
def cardChecker(card):
    win_nums = card[0]
    our_nums = card[1]
    matches = 0
    for win_num in win_nums:
        if win_num in our_nums:
            matches += 1
    return matches



scratches = 0
for card in data:
    card.append(1)

for index,card in enumerate(data):
    copy_num = cardChecker(card)
    for cycle in range(card[2]):
        for oneUp in data[index+1:index+copy_num+1]:
            oneUp[2] +=1
    


for x in data:
    scratches += x[2]




print(scratches)
    
    



 






    



