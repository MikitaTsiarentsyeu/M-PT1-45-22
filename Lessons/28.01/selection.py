l = [-60,3,6,1,3,7,9,54,9,-45,2,4,6]

for i in range(len(l)):
    m = i
    j = i + 1
    while j < len(l):
        if l[j] < l[m]:
            m = j
        j += 1
    l[i], l[m] = l[m], l[i]
    print(l)

print(l)
    