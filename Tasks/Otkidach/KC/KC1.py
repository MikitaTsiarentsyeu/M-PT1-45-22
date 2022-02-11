wrd = {"one": 1, "two": 2,"three": 3, "four": 4, "five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9,"ten": 10,"eleven": 11,"twelve": 12,"thirteen": 13,
"fourteen": 14,"fifteen": 15,"sixteen": 16,"seventeen": 17,"eighteen": 18,"nineteen": 19,"twenty": 20,"twenty one": 21}

v = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
v = v.split()
print(v)
# ['five', 'thirteen', 'two', 'eleven', 'seventeen', 'two', 'one', 'thirteen', 'ten', 'four', 'eight', 'five', 'nineteen']

l = []
for i in v:
    if i in wrd.keys():
        l.append(wrd[i])
print(l)
# [5, 13, 2, 11, 17, 2, 1, 13, 10, 4, 8, 5, 19]

b = []
for item in l:
    if item not in b:
       b.append(item) 
print(b)
# [5, 13, 2, 11, 17, 1, 10, 4, 8, 19]

b.sort()
print(b)
# [1, 2, 4, 5, 8, 10, 11, 13, 17, 19]

x=0
for n in b:
    if n%2 !=0:
        x += n
print(x)
#66  
