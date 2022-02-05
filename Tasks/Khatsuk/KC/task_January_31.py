import math
s = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen seven twelve'
s = s.split(' ')
s = [{'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,'seven':7,
    'eight':8, 'nine':9, 'ten':10,
    'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15,
    'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
    'twenty':20}[s] for s in s]
print(f'числа{s}')
s = list(set(s))
s.sort()
print(f'сортированные без дубликатов: {s}')
print(f'сумма элементов: {sum(filter(lambda s: s % 2 == 1, s))}')
#дополняем список бесконечностю, чтобы последняя пара не пропала после zip
#когда количесвто элементов в строке четное, а пар - нечетное
while len(s) % 2 == 0 :
    s.append(math.inf)
#делаем срезы строки со страйдом 2, сдвинутые на один элемент
#объединяем попарно в кортежи, получаем два списка кортежей
#из первого списка делаем список произведений, из второго - список сумм
#объединяем два списка в список кортежей
s = list(zip(
            map(lambda s:s[0]*s[1],
                zip(s[0::2], s[1::2])),
            map(lambda s:s[0]+s[1],
                zip(s[1::2], s[2::2])),
            )
        )
#убираем бесконечности
s = list(
    map(lambda s:(s[0], s[1] if s[1] != math.inf else None),s)
        )
print(s)


