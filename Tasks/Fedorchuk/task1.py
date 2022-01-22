import math
x = int(input("начальная сумма вклада "))
s = int(input("годовая ставка в процентах "))
m = int(input("срок вклада в годах "))
y = x*math.pow(1+(s/(12*100)),m*12)
print(int(y),"BYN")

