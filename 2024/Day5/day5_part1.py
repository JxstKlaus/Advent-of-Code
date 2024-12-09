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

correct_order_list = []
for order in orders:
    correct_order = True
    for i in range(len(order)-1):
        if order[i] not in rules and order[-1] != order[i]:
            correct_order = False
            break
        elif order[i+1] not in rules[order[i]]:
            correct_order = False
            break
    if correct_order:
        correct_order_list.append(order)

print("Day 5 part 1: ", sum([x[len(x)//2] for x in correct_order_list]))