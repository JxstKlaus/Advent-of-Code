use_real_data = True
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
        temp = {}
        rules = rules.split(",")
        for rule in rules[:-1]:
            rule = rule.split(":")
            temp[rule[0]] = rule[1]
        workflows[name] = temp,rules[-1][:-1]

    
    for part in data[data.index("")+1::]:
        part = part[1:-1].split(",")
        
        temp = {}
        for category in part:
            category = category.split("=")
            temp[category[0]] = int(category[1])
        parts.append(temp)

def ruleDecoder(workflow,part):
    for rule in workflow[0]:
        match rule[1]:
            case ">":
                if part[rule[0]] > int(rule[2:]):
                    return workflow[0][rule]
            case "<":
                if part[rule[0]] < int(rule[2:]):
                    return workflow[0][rule]
            case "=":
                if part[rule[0]] == int(rule[2:]):
                    return workflow[0][rule]
    return workflow[1]



total_rating = 0
for part in parts:
    workflow_name = "in"
    while True:
        if workflow_name == "A":
            total_rating += sum([part[x] for x in part])
            break
        elif workflow_name == "R":
            break
        workflow_name = ruleDecoder(workflows[workflow_name],part)
        
print(total_rating)




