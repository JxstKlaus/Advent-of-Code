example = ['rn=1','cm-','qp=3','cm=2','qp-','pc=4','ot=9','ab=5','pc-','pc=6','ot=7']

with open("2023\Day15\day15_input.txt", "r") as f:
    sequence = f.readline().split(",")
    

use_real_data = True
if not use_real_data:
    sequence = example

def valueCalc(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value*17) % 256
    return value


hashmap = {}
boxes = [[]] * 256

for step in sequence:
    if '=' in step:
        add_label = step[0:-2]
        if add_label not in hashmap:
            hashmap[add_label] = valueCalc(add_label)

        add_label_index = hashmap[add_label]
        if boxes[add_label_index] == []:
            boxes[add_label_index] = [step]
        else:
            found = False
            for i,lens in enumerate(boxes[add_label_index]):
                if lens[0:-2] == add_label:
                    boxes[add_label_index][i] = step
                    found = True
                    break
            if found == False:
                boxes[add_label_index].append(step)
        
    else:
        remove_label = step[0:-1]
        if remove_label not in hashmap:
            hashmap[remove_label] = valueCalc(remove_label)

        remove_label_index = hashmap[remove_label]
        for lens in boxes[remove_label_index]:
            if lens[0:-2] == remove_label:
                boxes[remove_label_index].remove(lens)

#[['rn=1', 'cm=2'], [], [], ['ot=7', 'ab=5', 'pc=6']]
#ot: 4 (box 3) * 1 (first slot) * 7 (focal length) = 28

def focusPower(box_index, lens_index, lens):
    return (box_index+1) * (lens_index+1) * int(lens[-1])

total_power = 0
for b_index, box in enumerate(boxes):
    for l_index, lens in enumerate(box):
        total_power += focusPower(b_index, l_index, lens)

print(f"part 2 answer: {total_power}")


