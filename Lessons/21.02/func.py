from functools import reduce

def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)


l = [1,2,3,4,5]
# apply(l, print)

def square(x):
    print(x*x)

# apply(l, square)

l = [1,2,3,4,5,6,7,8,9,10]

def search(l, el, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2
    if l[mid] == el:
        return mid
    elif l[mid] > el:
        return search(l, el, low, mid-1)
    else: 
        return search(l, el, mid+1, high)

print(search(l, 6, 0, len(l)-1))

print((lambda x: x*2)(10))

# def double(x):
#     return x*2

double = lambda x: x*2
print(double(2), double(20), double(200))

sum = lambda x, y, z=10: x+y+z
print(sum(1,2))

print(sorted("Abc aaa ttt".split(), key=str.lower))

t = [(1, "one"), (3, "three"), (2, "two")]
print(sorted(t, key=lambda x: x[1]))

d = {1: "one", 3: "three", 2: "two"}
print(sorted(d, key=d.get))
print(sorted(d.items(), key=lambda x: x[1]))

print(list(map(double, l)))
# [double(x) for x in l]

print(list(map(lambda x: x**2, l)))
print(list(map(lambda x: -x, l)))
print(list(map(lambda x: str(x), l)))

print(list(map(str.lower, "Abc aaa ttt".split())))

print(list(map(lambda x, y, z: x+y+z, [1,2,3,4,5], [6,7,8,9,10], [11,12,13])))

print(list(filter(lambda x: x>4, l)))

print(list(map(lambda x: -x, filter(lambda x: x>4, l))))

l = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x, y: x + y, l))

print(reduce(lambda x, y: f"{x} {y}", l))
"1 2"
"1 2 3"
"1 2 3 4"
"1 2 3 4 5"

print(reduce(lambda x, y: x if x < y else y, l))