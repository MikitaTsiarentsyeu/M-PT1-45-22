a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = b ** 2 - 4*a*c
x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)
if d < 0:
    print ("Корней нет")
elif d == 0:
    x = (-b)/(2*a)
    print ("Корень = " + str(x))
else :
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print ("X1  = " + str(x1))
    print("X2 = " + str(x2))


    

