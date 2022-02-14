def maker(n):
    def action(x):
        return x ** n
    return action

square = maker(2)
cube = maker(3)

print(maker(3)(10))

for i in range(10):
    print(square(i), cube(i))
    