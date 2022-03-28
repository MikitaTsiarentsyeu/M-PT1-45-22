#1. Написать рекурсивную функцию для вычисления суммы 
# всех элементов вложенных (любая глубина) списков.

def sum_elements(list):
    sum = 0
    for elem in list:
        if isinstance(elem, int):       
            sum += elem
        else:
            sum += sum_elements(elem)
    return sum

list = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(sum_elements(list))

#2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.

def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    list_new = fib(n-1)
    list_new.append(list_new[-1] + list_new[-2])
    return list_new

print(fib(5))
print(fib(10))