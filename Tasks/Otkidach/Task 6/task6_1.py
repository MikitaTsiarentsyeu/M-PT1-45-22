# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum1(l):
    i = 0
    for element in l:
        if (isinstance(element, list)):
            i = i + sum1(element)
        else:
            i = i + element
    return i
print(sum1([1, 2, [2, 4, [[7, 8], 4, 6]]]))
