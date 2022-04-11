# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

n = int(input("Введите число: "))
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n
l = []
for i in range(n):
    l.append(fib(i))
print(l)
