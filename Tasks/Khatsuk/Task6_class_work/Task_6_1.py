def list_sum(l):
    'рекурсивная функция для вычисления суммы списка (вложенных списков)'
    sum = 0

    for i in l :
        #если элемент списка - список, то запускаем функцию
        if isinstance(i, list):
            sum += list_sum(i)
        #если нет, то суммируем
        else:
            sum += i
    return sum

print(list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))