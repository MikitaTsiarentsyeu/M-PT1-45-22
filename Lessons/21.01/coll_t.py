t = (1,2,3,45,"test")

print(t, type(t))

t = ()
print(t, type(t))

t = ("1",)
print(t, type(t))

#t[0] = 1
#t.append(1)

t = ((1,2,3,4,5)+(6,7,8,9))*3
print(t)

print(t.index(1))

print(len(t), id(t))

l = list(t)
print(l)

del l[5:16]
t = tuple(l)
print(t, id(t))

del t