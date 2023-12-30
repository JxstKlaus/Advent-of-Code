example = [
    [0, 3, 6, 9, 12, 15], #18
    [1, 3, 6, 10, 15, 21], #28
    [10, 13, 16, 21, 30, 45] #68
]

with open("Day9\day9_input.txt", "r") as f:
    history = [list(map(int, line.strip().split())) for line in f]

use_real_data = True
if not use_real_data:
    history = example

def nextValue(hist):
    pred_list = [hist+["A"]]
    while True:
        hist = pred_list[-1]
        diff = [hist[i]-hist[i-1] for i in range(1,len(hist[0:-1]))]
        if set(diff) == {0}:
            pred_list.append(diff + [0])
            break
        pred_list.append(diff + ["A"])
    
    pred_list = [line[::-1] for line in pred_list][::-1]

    for i in range(len(pred_list)-1):
        pred_list[i+1][0] = pred_list[i+1][1] + pred_list[i][0]

    return pred_list[-1][0]

total = 0
for hist_line in history:
    total += nextValue(hist_line)

print(f"Part 1 answer: {total}")

