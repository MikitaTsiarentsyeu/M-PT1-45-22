print('a' == "a" == """a""")

x = """ the first line
    the second line
    the third line
"""

print(x)
print(repr(x))

print("value = \test\' ")

print(len(""), len("meaningful string"), len("\t"))
x = "str1 " + "str2 " + "str3"
print(x)

x = "Na"*14 + " Batman!"
print(x)

s = "my very long string"
print(s[0], s[1])
print(s[len(s)-1]) #[18] - the last one
print(s[-1], s[-2], s[-3])
print(s[-19]) # the first one

print(s[1:5])
print(s[:5])
print(s[5:])
print(s[::-1])

# s[4] = "test"
s = "test"