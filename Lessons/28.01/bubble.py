l = [-60,3,6,1,3,7,9,54,9,-45,2,4,6]

# l.sort()
sorted(l)

#l = [-60, -45, 1, 2, 3, 3, 4, 6, 6, 7, 9, 9, 54]

for y in range(len(l)):
    for x in range(len(l)-1):
        if l[x] > l[x+1]:
            l[x], l[x+1] = l[x+1], l[x]
    print(l)

print(l)