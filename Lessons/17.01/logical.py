x = 10


# if x == 0:
#     print("it's zero")
# elif x == 1:
#     print("it's one")
# elif x == 2:
#     print("it's two")
# elif x == 3:
#     print("it's three")

if x > 0:
    print("it's positive")
elif x == 0:
    print("it's zero")
else:
    print("it's negative")

print("it's positive") if x > 0 else print("it's zero") if x == 0 else print("it's negative")


if x >= 0:
    if x == 0:
        print("it's zero")
    else:
        print("it's positive")
else:
    print("it's negative")

if x == 10:
    y = "correct!"
else:
    y = "not so good"

print("correct!") if x == 10 else print("not so good")

y = "correct!" if x == 10 else "not so good"
print(y)