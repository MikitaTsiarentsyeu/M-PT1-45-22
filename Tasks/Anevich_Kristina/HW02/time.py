import datetime as dt

dict_m = {
1: ['одна', 'одной'], 2: ['две', 'двух'], 3: ['три', 'трех'],
4: ['четыре', 'четырёх'], 5: ['пять', 'пяти'], 6: ['шесть', 'шести'],
7: ['семь', 'семи'], 8: ['восемь', 'восьми'], 9: ['девять', 'девяти'],
10: ['десять', 'десяти'], 11: ['одинадцать', 'одинадцати'], 
12: ['двенадцать', 'двенадцати'], 13: ['тринадцать', 'тринадцати'],
14: ['четырнадцать', 'четарнадцати'], 15: ['пятнадцать', 'пятнадцати'],
16: ['шестнадцать'], 17: ['семнадцать'], 18: ['восемнадцать'], 19: ['девятнадцать'],
20: ['двадцать'], 30: ['тридцать'], 40: ['сорок'], 50: ['пятьдесят']
}

dict_h = {
0: ['ноль'],
1: ['час', 'первого'],
2: ['два', 'второго'],
3: ['три', 'третьего'],
4: ['четыре', 'четвертого'],
5: ['пять', 'пятого'],
6: ['шесть', 'шестого'],
7: ['семь', 'седьмого'],
8: ['восемь', 'восьмого'],
9: ['девять', 'девятого'],
10: ['десять', 'десятого'],
11: ['одинадцать', 'одинадцатого'],
12: ['двенадцать', 'двенадцатого'],
}

print('Если хочешь узнать время, ты можешь нажать:\n1 - вывести текущее время\n2 - набрать время вручную\n')

choice = int(input('Введите номер необходимого действия:  '))
if choice == 1:
    time = dt.datetime.now().time()
    time = time.strftime('%H:%M')
    print(time)
elif choice == 2:
    time = input('Введите время в диапазоне от 00:00 до 23:59 в формате HH:ММ :   ')
    time = time.replace(' ', '')

time = time.split(':')
min = int(time[1])
h = int(time[0])

h1 = h
h = h - 12 if h > 11 else h
minutes = ''

if min == 1 or min == 21 or min == 31 or min == 41:
    minutes = 'минута'
elif 1 < min < 5 or 21 < min < 25 or 31< min <35 or 41 < min < 45:
    minutes = 'минуты'
elif 4 < min < 20 or 24 < min < 30 or 34 < min < 40 or 44 < min <59:
    minutes = 'минут'

if min == 0:
    h1 = h1 - 12 if h1 > 12 else h1
    end = ''
    if h1 == 1:
        print('час ровно')
    else:
        if h1 == 0 or 5 <= h1 <= 12:
            end = 'ов'
        elif 1 < h1 < 5:
            end = 'а'
        print(f'{dict_h[h1][0]} час{end} ровно')

elif min < 30 or 30 < min < 45:
    if 0 < min < 21 or min == 40:
        print(f'{dict_m[min][0]} {minutes} {dict_h[h+1][1]}')
    elif 20 < min < 45:
        print(f'{dict_m[min-min%10][0]} {dict_m[min%10][0]} {minutes} {dict_h[h+1][1]}')

elif int(min) == 30:
    print(f'половина {dict_h[h+1][1]}')

elif min >= 45:
    print(f'без {dict_m[60-min][1]} {minutes} {dict_h[h+1][0]}')
    