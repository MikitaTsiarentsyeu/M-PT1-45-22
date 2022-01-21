l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0.0, "test", []]

print(l, type(l))

print(list())
print(list("test str"))

print(([1,2,3]+[4,5,6])*4)

print(l[0], l[1], l[2])
print(l[-2])

print(l[0:5:2])
print(l[::-1])

print(len(l))

l.append("new elem")
print(l)

l[9] = 0
print(l)

l.extend([9,8,7,6,5,4,3,2,1])
print(l)

l.insert(0, "new first elem")
print(l)

l.insert(100, "new last elem")
print(l)

l[1:13] = ["new new elem"]
print(l)

print(l.pop(), l)
print(l.pop(0), l)

print(l.index('new elem'))
print(l.pop(l.index('new elem'))) #danger
# print(l.index(345678)) ERROR

l.remove(9)
print(l)

print(8 in l, 9 in l)

del l[0]
del l[0:4]
print(l)

l.clear()
print(l)

del l
# print(l)