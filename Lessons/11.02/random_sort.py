import random

l = [1,7,2,6,4,5,8]

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0,n-1)

def swap(l):
    x, y = generate_index(len(l)), generate_index(len(l))
    while x == y:
        y = generate_index(len(l))

    l[x], l[y] = l[y], l[x]

def sort(l):
    count = 0
    while not is_sorted(l):
        count += 1
        print("***")
        swap(l)
    print(count)

# sort(l)
# print(l)

random.shuffle(l)
print(l)

def generate_indexes(n):
    s = []
    while len(s) != n:
        x = generate_index(n)
        if x not in s:
            s.append(x)
    return s

s1, s2 = generate_indexes(len(l)), generate_indexes(len(l))

print(s1, s2)

def shuffle(l, s1, s2):
    for i in range(len(l)):
        l[s1[i]], l[s2[i]] = l[s2[i]], l[s1[i]]

for i in range(100):
    shuffle(l, s1, s2)
    print(l)