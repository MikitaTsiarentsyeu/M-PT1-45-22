eq = input("Enter your eq:")
print(eq)
x = input("Enter your x:")
x = int(x)
print(x)

# eq = "   y   =   10   x   -  34"
# x = 0

eq = eq.replace(' ','').replace('y=','')
eq = eq.split('x')

print(int(eq[0])*x+int(eq[1]))
