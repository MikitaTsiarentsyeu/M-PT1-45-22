from sympy import per


s = {1,2,2,2,2,2,2,2,2,2,3,4,"test"}
print(type(s), s)

# s = {1,2,[3,4]} error

s = set([1,1,1,1,1,1,1])
print(s)

l = [1,2,3,3,4,4,5]
l = list(set(l))
print(l)

#s = {}
s = set()
print(type(s))

s.add(1)
s.add(1)
print(s)

s.update("aaasssdddfff")
print(s)

s.add((2,3,4))
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
print(s)

s = {1,2,3,4,5}
s.remove(1)
print(s)
# s.remove(1)
s.discard(1)
print(s)

s.clear()
print(s)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.intersection(s2))
print(s1.union(s2))

print({1,2,3}.issubset({1,2,3,4}))

str1 = "test"
str2 = "tset"
print(str1==str2, set(str1)==set(str2))