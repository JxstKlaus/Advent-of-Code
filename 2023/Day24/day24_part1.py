example = [
[(19, 13, 30) ,(-2,  1, -2)],
[(18, 19, 22) ,(-1, -1, -2)],
[(20, 25, 34) ,(-2, -2, -4)],
[(12, 31, 28) ,(-1, -2, -1)],
[(20, 19, 15) ,( 1, -5, -3)],
]

with open("2023\Day24\day24_input.txt", "r") as f:
    data = [[tuple(map(int, x.split(", "))),tuple(map(int, y.split(", ")))] for x,y in [line.strip().split(" @ ") for line in f]]


min_pos = 200000000000000
max_pos = 400000000000000

use_real_data = True
if not use_real_data:
    min_pos = 7
    max_pos = 27
    data = example

def det2x2(col1,col2):
    return col1[0]*col2[1] - col2[0]*col1[1]

def oppositeVect(vect):
    return (-vect[0],-vect[1])

def divVect(vect1,vect2):
    return (vect1[0]-vect2[0],vect1[1]-vect2[1])

#solving the equation for t and u with matrices:
#A+velocity1*t = B+velocity2*u
#A,B are points; v1,v2 are vectors;
#-----------------------------------------------
#velocity1[0]-velocity2[0] = (B[0]-A[0])
#velocity1[1]-velocity2[1] = (B[1]-A[1])

count = 0
for i,(A,velocity1) in enumerate(data):
    for j, (B,velocity2) in enumerate(data[i+1::]):
        det = det2x2(velocity1,oppositeVect(velocity2))
        det_delta1 = det2x2(divVect(B,A),oppositeVect(velocity2))
        #det_delta2 = det2x2(velocity1,divVect(B,A))
        if det != 0:
            #if I were to use det_delta2 value then I had to also replace A with B  ---> it doesn't matter, solution is the same
            intersection = A[0] + velocity1[0]*(det_delta1/det), (A[1] + velocity1[1]*(det_delta1/det))
            if min_pos <= intersection[0] <= max_pos and min_pos <= intersection[1] <= max_pos:
                if (intersection[0]-A[0])/velocity1[0] >= 0 and (intersection[1]-A[1])/velocity1[1] >= 0 and (intersection[0]-B[0])/velocity2[0] >= 0 and (intersection[1]-B[1])/velocity2[1] >= 0:
                    count+= 1
print(f"Day 24 part 1 answer: {count}")