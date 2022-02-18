def elements_counter(base_collection):
    "возвращает список кортежей из переданной коллекции: (элемент коллекции:частота встречаемости)"
    elements_dict = dict.fromkeys(set(base_collection),0)
    for element in base_collection:
        elements_dict[element] +=1
    elements_list =list(elements_dict.items())
    #список сортируется по частоте встречаемости(от большей к меньшей) и элементу коллекции"
    elements_list.sort(key = lambda t: (-1*t[1], t[0]), reverse = False)
    return elements_list
def raz_or_raza(number):
    "возвращает 'раз' или 'раза' для заданного числа"
    if (2 <= number % 10 <=4) and (number % 100 not in [12, 13, 14] ) :
        return 'раза'
    else:
        return 'раз'
def answer(elements_list, number):
    "печатает ответ для заданного количества элеметнов "
    for i in range(number):
        print('{} встречается {} {}'.format(repr(elements_list[i][0]),elements_list[i][1],
                raz_or_raza(elements_list[i][1])))
while True :
    base_string = input('Введите строку:')
    if not base_string:
        print('нужна не пустая строка !!!!!!')
        continue
    else:
        #если в коллекции есть элементы, то высчитываем их количество
        result_list = elements_counter(base_string)
    #цикл прекращается, когда введена цифра от 1 до количества элементов
    while True:
        elements_qantity = input('Введите количество элементов в ответе:')
        if elements_qantity.isdigit():
            elements_qantity = int(elements_qantity)
            if 0 < elements_qantity <= len(result_list):
                break
            else:
                print('нужна цифра от одного до количества элементов!!!!!!')
                print(f'в нашей строке только {len(result_list)}!!!!!')
        else:
             print('нужна цифра !!!!!!')
    answer(result_list, elements_qantity)






