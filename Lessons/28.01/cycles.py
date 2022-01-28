import random

counter = 0

# while True:
#     print(f"I'm going!!! - {counter}")
#     counter += 1

while counter < 10:
    print(counter)
    counter += 1

print("after a while")

l = [1,2,3,4,5]

for x in l:
    print(x)
    x = 10
    print(x)

print(l)

for s in "my test str":
    print(s)

for s in (6,7,8,9):
    print(s)

d = {1:"one", 2:"two"}
print(list(d))

for x in d:
    print(f"key - {x}, value - {d[x]}")

for x in d.values():
    print(f"value - {x}")

for k, v in d.items():
    print(f"key - {k}, value - {v}")

# for x in l:
#     print(x)
#     l.pop()

# for x in l:
#     del l[0]
#     print(l)

# for x in l:
#     l.append(random.randint(0, 10))
#     print(l)

# for i, x in enumerate(l):
#     del l[0]
#     print(i, l)

ind_to_del = []
for i, x in enumerate(l):
    if x%2 == 0:
        ind_to_del.append(i)

print(ind_to_del)
for i in ind_to_del[::-1]:
    del l[i]

print(l)

counter = 0
while counter < len(l):
    print(l[counter])
    counter += 1

l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for x in l:
    print(x)
    for y in x:
        print(y)

for x in range(0, 10, 2):
    print(x)

for x in range(len(l)):
    print(l[x])


l = [1,2,3,4,5,6,7,8,9,10]

for x in l:
    if x == 3:
        continue
    if x == 6:
        continue
    if x > 8:
        break
    print(x)
else:
    print("hello from else")

while True: pass