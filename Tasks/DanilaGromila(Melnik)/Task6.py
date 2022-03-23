def deep_recursive(lst):
    '''рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков'''
    summary = 0
    for item in lst:
        if isinstance(item, list):
            summary += deep_recursive(item)
        else:
            summary += item
    return summary


print(deep_recursive([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n):
    if n > 2:
        total = fib(n - 1)
        total += total[-2] + total[-1],
        return total
    elif n == 2:
        return 0, 1
    else:
        return 0


print(fib(10))

