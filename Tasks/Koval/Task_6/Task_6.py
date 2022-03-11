# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def sum_all_elem_of_list(l):
    sum = 0
    for elem in l:
        if isinstance(elem,list):
            sum += sum_all_elem_of_list(elem)
            continue
        sum += elem
    return sum

l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print (sum_all_elem_of_list(l))

def fib(n, first=0, second=1, output='0, 1',counter=2):
    if n <= 1:
        return 0
    if counter == n:
        return output
    return fib(n,second,first+second,f'{output}, {first+second}', counter+1)


print(fib(1))
print(fib(2))
print(fib(5))
print(fib(10))


