example = [
        ["32T3K", "765"],
        ["T55J5", "684"],
        ["KK677", "28"],
        ["KTJJT", "220"],
        ["QQQJA", "483"]]

with open("Day7\day7_input.txt", "r") as f:
    data = [line.strip().split() for line in f]

use_real_data = True
if not use_real_data:
    data = example

data = [(hand, int(bid)) for hand,bid in data]

#separating the hands by type

five = []
four = [] 
full_house = []
three = [] 
two_pair = [] 
one_pair = [] 
high_card = [] 

for hand,bid in data:
    jokers = hand.count("J")
    no_joker = hand.replace("J","")

    card_counts = []
    for card in set(list(no_joker)):
        card_counts.append((card, hand.count(card)))

    if len(card_counts) == 0:
        best = jokers
    else:
        best = max([x[1] for x in card_counts])+jokers

    match best:
        case 5:
            five.append((hand,bid))
        case 4:
            four.append((hand,bid))
        case 3:
            if len(card_counts) == 2:
                full_house.append((hand,bid))
            else:
                three.append((hand,bid))
        case 2:
            if len(card_counts) == 4:
                one_pair.append((hand,bid))
            elif len(card_counts) == 3:
                two_pair.append((hand,bid))
        case 1:
            high_card.append((hand,bid))


#hands = types from lowest to highest
hands = [high_card, one_pair, two_pair, three,full_house, four, five]

#assigning a number to each letter considering it's strength
dictionary = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10
}

def letter_to_num(hand): #hand = "QQQJA"
    return [dictionary[card] if card in dictionary else int(card) for card in hand]



numberized_cards = []
for type in hands:
    temp_type = []
    for hand,bid in type:
        temp_type.append((letter_to_num(hand),bid))
    numberized_cards.append(temp_type)


#sorting the (hand,bid) tuples by the first value
    
sorted_numberized_cards = []
for type in numberized_cards:
    sorted_numberized_cards += (sorted(type, key = lambda x:x[0]))

#print(sorted_numberized_cards)
winnings = 0
for i,bid in enumerate(sorted_numberized_cards):
    winnings += bid[1]*(i+1)

print(f"Answer to part 1: {winnings}")