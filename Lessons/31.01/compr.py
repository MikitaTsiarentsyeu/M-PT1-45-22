from re import X


print(range(10))

l = [x for x in range(10)]
print(l)

# l = []
# for x in range(10):
#     l.append(x)
# print(l)

l = [(x**3)+100500 for x in range(10)]
print(l)

l = [x for x in "my test str" if x != ' ' if x != 't']
print(l)

# l = []
# for x in "my test str":
#     if x != ' ':
#         if x != 't':
#             l.append(x)
# print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
l = [y for x in l for y in x]
print(l)

# l = []
# for x in l:
#     for y in x:
#         l.append(y)

l1 = [1,2,3,4,5]
#l2 = [1,2,3,4,5]
l2 = [1,2,3,4,5,6,7,8,9,0]

l = [[x**y for x in l1] for y in l2]
print(l)

d = {x:str(x) for x in range(10)}
print(d)

l = [str(k)+v for k, v in d.items()]
print(l)