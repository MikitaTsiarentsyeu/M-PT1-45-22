import datetime


hours = {1: 'один час', 2: 'два часа', 3: 'три часа', 4: 'четыре часа', 5: 'пять часов', 6: 'шесть часов',
         7: 'семь часов', 8: 'восемь часов', 9: 'девять часов', 10: 'десять часов', 11: 'одиннадцать часов',
         12: 'двенадцать часов'}
hours_case = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвертого', 5: 'пятого', 6: 'шестого',
              7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: 'десятого', 11: 'одиннадцатого',
              12: 'двенадцатого'}
minutes = {1: 'одна минута', 2: 'две минуты', 3: 'три минуты', 4: 'четыре минуты', 5: 'пять минут',
           6: 'шесть минут', 7: 'семь минут', 8: 'восемь минут', 9: 'девять минут', 10: 'десять минут',
           11: 'одиннадцать минут', 12: 'двенадцать минут', 13: 'тринадцать минут', 14: 'четырнадцать минут',
           15: 'пятнадцать минут', 16: 'шестнадцать минут', 17: 'семнадцать минут', 18: 'восемнадцать минут',
           19: 'девятнадцать минут', 20: 'двадцать минут', 21: 'двадцать одна минута',
           22: 'двадцать две минуты', 23: 'двадцать три минуты', 24: 'двадцать четыре минуты',
           25: 'двадцать пять минут', 26: 'двадцать шесть минут', 27: 'двадцать семь минут',
           28: 'двадцать восемь минут', 29: 'двадцать девять минут', 31: 'дридцать одна минута',
           32: 'тридцать две минуты', 33: 'тридцать три минуты', 34: 'тридцать четыре минуты',
           35: 'тридцать пять минут', 36: 'тридцать шесть минут', 37: 'тридцать семь минут',
           38: 'тридцать восемь минут', 39: 'тридцать девять минут', 40: 'сорок минут', 41: 'сорок одна минута',
           42: 'сорок две минуты', 43: 'сорок три минуты', 44: 'сорок четыре минуты'}
minutes_remain = {45: 'пятнадцати минут', 46: 'четырнадцати минут', 47: 'тринадцати минут', 48: 'двенадцати минут',
                  49: 'одиннадцати минут', 50: 'десяти минут', 51: 'девяти минут', 52: 'восьми минут',
                  53: 'семи минут', 54: 'шести минут', 55: 'пяти минут', 56: 'четырех минут',
                  57: 'трех минут', 58: 'двух минут', 59: 'одной минуты'}

print('Вы хотите ввести текущее время с клавиатуры? да/нет')
answer_1 = input()
if answer_1 == 'да':
    print('введите текущее время в формате hh:mm')
    time_1 = input()
    time_1 = str(time_1).split(':')
    hh_1 = int(time_1[0])
    mm_1 = int(time_1[1])

    if mm_1 == 0:
        print(f'{hours[hh_1%12]} ровно')
    elif 0 < mm_1 < 30 or 30 < mm_1 < 45:
        print(f'{minutes[mm_1]} {hours_case[hh_1%12+1]}')
    elif mm_1 == 30:
        print(f'половина {hours_case[hh_1%12+1]}')
    elif 45 <= mm_1 < 60:
        print(f'без {minutes_remain[mm_1]} {hours_case[hh_1%12+1]}')
    quit()

elif answer_1 == 'нет':
    print('Вы хотите узнать текущее время? да/нет')
answer_2 = input()
if answer_2 == 'да':
    time_2 = datetime.datetime.now().time()
    time_2 = str(time_2).split(':')
    hh_2 = int(time_2[0])
    mm_2 = int(time_2[1])

    if mm_2 == 0:
        print(f'{hours[hh_2]} ровно')
    elif 0 < mm_2 < 30 or 30 < mm_2 < 45:
        print(f'{minutes[mm_2]} {hours_case[hh_2%12+1]}')
    elif mm_2 == 30:
        print(f'половина {hours_case[hh_2%12+1]}')
    elif 45 <= mm_2 < 60:
        print(f'без {minutes_remain[mm_2]} {hours_case[hh_2%12+1]}')
else:
    print('ну как хотите')
