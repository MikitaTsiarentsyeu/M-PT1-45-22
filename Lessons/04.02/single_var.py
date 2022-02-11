s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

s = [{"five": 5, "thirteen": 13, "two": 2, "eleven": 11, "seventeen": 17, "one": 1, "ten": 10, "four": 4, "eight": 8, "nineteen": 19}[s] for s in s.split()]
print(s)

s = list(set(s))
print(s)

s += [True, 0, 0]
print(s)

while True:

    print(s)

    if s[s[-1]] % 2 != 0:
        s[-2] += s[s[-1]]

    if type(s[s[-1]+1]) == type(True):
        break

    if s[-3]:
        print(f"{s[s[-1]]} * {s[s[-1]+1]} = {s[s[-1]]*s[s[-1]+1]}")
    else:
        print(f"{s[s[-1]]} + {s[s[-1]+1]} = {s[s[-1]]+s[s[-1]+1]}")

    # print(s[s[-1]])

    s[-1] += 1
    s[-3] = not s[-3]

print(f"total is {s[-2]}")