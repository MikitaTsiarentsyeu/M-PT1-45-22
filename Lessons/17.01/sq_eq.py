message = "Please input value of "
a, b, c = input(message + "a:"), input(message + "b:"), input(message + "c:")

a, b, c = int(a), int(b), int(c)

print(a,b,c)

D = b*b - 4*a*c

if D < 0:
    print("There are no roots")
elif D == 0:
    x = (-b)/(2*a)
    print(x)
else:
    x_1 = (-b + D**0.5) / (2*a)
    x_2 = (-b - D**0.5) / (2*a)
    print(x_1, x_2)
