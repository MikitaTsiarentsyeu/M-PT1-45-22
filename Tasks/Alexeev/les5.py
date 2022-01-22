from tkinter import Y


eq = input("Enter your eq: ")
print(eq)
x = input(" Enter your x: ")
x = int(x)
print(x)
eq = eq.replace(' ','').replace('y=','')

eq = eq.split('x')
print(int(eq[0])*+int(eq[1]))