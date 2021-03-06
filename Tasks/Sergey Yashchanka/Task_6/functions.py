# Задание:

# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова:
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34
# 3. Task from class

# ------------------------------------------------------------------------------------------------------------------ #

# Решение:
# 1
any_list = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def summary(array, summa=0):
    """используя необычную распаковку списка решил сделать эту задачу без использования цикла!!!
    пример:
    list = [1, 2, 3, 4, 5]
    first, second, third, forth, fifth = list"""
    num, *remainder = array  # распаковываем список: кладем в num первое число а остальные в remainder
    if num and not remainder:  # если num не пустой а remainder пустой! такое бывает, когда список в списке!
        array = num  # в список кладем список достав его из основного списка
        num = 0  # в этом случае в num кладем ноль
    else:
        if isinstance(num, list):  # если в нам попадает не одно число, а список!
            num = sum(num)  # то складываем числа в списке и в нам кладем сумму всех чисел списка
        array = remainder  # в основной список кладем остаток
    if isinstance(array, int):  # БАЗОВЫЙ СЛУЧАЙ! если распаковали все списки и число осталось без списка!
        return summa + array  # плюсуем его к результату
    return summary(array, summa + num)  # РЕКУРСИВНЫЙ СЛУЧАЙ! вызывает саму себя и складываетчисла


print(summary(any_list))  # 34


# 2
def fibonacci(n, result='', count=0):
    """это не самое быстрое но забавное решение содержит в себе две рекурсивных функции одна из корорых лямбда функция
    присвоенная переменной рекурсия в рекурсии! функция 'fibonacci' на прямом ходу генерирует числа фибоначчи с помощью
    лямбда рекурсивной функции 'fib' которая высчитывает число фибоначчи равное n на обратном ходу!"""
    if count == n:  # если счетчик равен колличеству запросов! БАЗОВЫЙ СЛУЧАЙ!
        return result[:-1]  # возвращаем нужное колличество запрошенных вычесленных чисел фибоначчи

    # возвращает число фибоначчи равное n по очереди начиная с нуля
    fib = (lambda x: fib(x - 1) + fib(x - 2) if x > 2 else (0 if x == 0 else 1))

    # РЕКУРСИВНЫЙ СЛУЧАЙ!

    return fibonacci(n, f'{result}{fib(count)},', count + 1)  # вызывая саму себя прибавляет в результат числа фибоначчи


print(fibonacci(10))  # 0,1,1,2,3,5,8,13,21,34

# 3
l = ["1", "11", "12", "22", "2", "13", "30", "33"]
# выводит список четных корней и сортирует его по возрастанию
print(list(filter(lambda x: (int(x) * int(x)) % 2 == 0, sorted(l, key=lambda x: int(x)))))  # ['2', '12', '22', '30']
