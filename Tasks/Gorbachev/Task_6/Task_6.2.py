"""2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
Примеры вызова: 
fib(5) -> 0,1,1,2,3
fib(10) -> 0,1,1,2,3,5,8,13,21,34"""
import random

dict_fib = {1: 0, 2: 1} # initial two elements of Fibonacci sequence, what gives us limiting position of depth of recursion

def fib(elem):
    """Return elements of Fibonacci sequence
    
    Parameters:
        elem: int
            user value of depth of Fibonacci sequence
    Returns:
        dict_fib[elem]: dict element (key: value)
            element of Fibonacci sequence (position: value)"""
    if elem in dict_fib: #limiting of depth of recursion
        return dict_fib[elem]
    dict_fib[elem] = fib(elem - 1) + fib(elem - 2)
    return dict_fib[elem] 


n = random.randint(2, 50) # generating random int number between 2 and 50
fib(n)
print(f'fib({n}) -> ', end= "")
print(*dict_fib.values(), sep = ', ') 