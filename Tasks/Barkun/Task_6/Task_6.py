# # 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# # Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

user_list = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def sum_elem(user_list):
    sum_elem_total = 0
    for element in user_list:
        if (type(element) == type([])):
          sum_elem_total = sum_elem_total + sum_elem(element)
        else:
          sum_elem_total = sum_elem_total + element
    return sum_elem_total
print("\nThe sum of all elements is equal to:", sum_elem(user_list))


# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def fibonacci(n):
    if (n < 2):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("\nEnter the number of sequence numbers:\n"))
print("\nThe Fibonacci sequence:")
for i in range(n):
    print(f'{fibonacci(i)}, ', end = '')

                                 
                                    #Дополнительная задача

# Отсортировать список по возрастанию числовых значений, исключив те, квадраты котрорых являются нечетными значениями
# ['1', '11', '12', '22', '2', '13', '30', '33']

user_list = ['1', '11', '12', '22', '2', '13', '30', '33']

                                    # Вариант в одну строку

print ('\n\n', str(sorted([ (int(elem))**2 for elem in user_list if ((int(elem))**2)%2 == 0])).strip('][').split(', '))

                                    # Вариант с фукцией "lambda"

l_lambda = lambda elem: (int(elem))**2
elem = sorted([l_lambda(elem) for elem in user_list if l_lambda(elem) %2 == 0])
print ('\n', ( str(elem).strip('][').split(', ')), '\n')

