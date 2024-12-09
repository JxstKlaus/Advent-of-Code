example = [
    {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},

    [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13],
        [75,97,47,61,53],
        [61,13,29],
        [97,13,75,29,47]
    ]

]

with open("2024/Day5/day5_input.txt", "r") as f:
    rules_raw, orders = f.read().split('\n\n')
    """rules = {
        27: [33, ..., 19]
    }"""
    rules = {}
    for rule in rules_raw.split("\n"):
        x,y = rule.split("|")
        if int(x) in rules:
            rules[int(x)].append(int(y))
        else:
            rules[int(x)] = [int(y)]
    orders = [list(map(int, x.split(","))) for x in orders.split("\n")]


use_real_data = True
if not use_real_data:
    rules = example[0]
    orders = example[1]

incorrect_order_list = []
for order in orders:
    correct_order = False
    iterations = 0
    while not correct_order:
        iterations += 1
        #checks if the order is correct by default
        #if it is then while loop ends with iterateions = 1
        #if iterations > 1 that means the order was not correct in the first place
        for i in range(len(order)-1):
            if order[i] not in rules and order[-1] != order[i]:
                order[i], order[-1] =  order[-1],order[i]
                break
            elif order[i+1] not in rules[order[i]]:
                order[i], order[i+1] =  order[i+1],order[i]
                break
        else:
            correct_order= True
    #only add if order modified
    if iterations > 1:
        incorrect_order_list.append(order)

print("Day 5 part 2: ", sum([x[len(x)//2] for x in incorrect_order_list]))