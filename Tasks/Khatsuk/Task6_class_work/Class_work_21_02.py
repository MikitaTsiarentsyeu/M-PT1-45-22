def exclusive_sort(l):

    #приводим к int
    result = map(int, l)
    #квадрат четного числа - четное, поэтому в квадрат не возводим
    #фильтруем и сортируем оставшиеся элементы
    result = sorted(filter(lambda x: x % 2 == 0, result))

    return list(map(str, result))

"""
def exclusive_sort_v0(l):

    #решение в лоб
    result = sorted(filter(lambda x: (int(x) % 2)**2 == 0, l), key=int)

    return list(result)
"""

l = [1, 11, 12, 22, 2, 13, 30, 33]
l = list(map(str, l))

print(exclusive_sort(l))
