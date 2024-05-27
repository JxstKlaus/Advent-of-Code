


use_real_data = False
if use_real_data:
    file = "day19_input.txt"
else:
    file = "day19_example.txt"

with open(f"2023\Day19\{file}","r") as f:
    data = [line.strip() for line in f]
    workflows = {}
    parts = []

    for workflow in data[:data.index("")]:
        name,rules = workflow.split("{")
        temp = [[],[]]
        rules = rules.split(",")
        for rule in rules[:-1]:
            a,b = rule.split(":")
            temp[0].append(a)
            temp[1].append(b)
        
        workflows[name] = [temp[0]+[True],temp[1]+[rules[-1][:-1]]]


#Returns True or False
def ruleDecoder(char_value: int,operator: str,digit: int):
    match operator:
        case ">":
            if char_value > digit:
                return operator, True
        case "<":
            if char_value < digit:
                return operator, True
    return operator, False



