import math

l = [-60,3,6,1,3,7,9,54,9,-45,2,4,6]

min = l[0]
for x in l:
    if min > x:
        min = x
    print(min)


min = [l[0], l[1]]
min_ind = 0
flag = True
for i, x in enumerate(l):
    if min[0] > x:
        min[1] = min[0]
        min[0] = x
        min_ind = i
    print(min, min_ind)