# Задание:

# Реализовать:
# 1
# .текстовый вывод текущего времени
# 2
# .текстовый вывод времени, введённого с консоли (hh :mm).
# (дать пользователю возможность выбрать режим работы программы)
#
# Для получения текущего времени использовать модуль datetime.
#
# min == 0: тако е -то значение часа ровно
# min < 30: стольк о -то минут следующего часа
# min == 30: половина таког о -то
# min > 30 and min < 45 стольк о -то минут следующего часа
# min >= 45 без min таког о -то
#
#
# 21 :16
# шестнадцать минут десятого

# ------------------------------------------------------------------------------------------------------------------ #

# Решение:

# from module import class
from datetime import datetime as dt

# get hours and minutes, translate format of time
got_time = dt.now().time()
got_hour = None
got_min = None

# user interaction
answer_user = input(
    "Здравствуйте! Если вы хотите получить текущее время введите: 'Y' либо введите время в формате 'hh:mm' | "
)

# check enter of user!! if enter is not correct, user get present time!
try:
    if 0 < int(answer_user[:answer_user.find(":")]) < 25 and -1 < int(
            answer_user[answer_user.find(":") + 1:]) < 60:
        got_hour = int(answer_user[:answer_user.find(":")]) % 12
        got_min = int(answer_user[answer_user.find(":") + 1:])
except ValueError:
    got_hour = got_time.hour % 12
    got_min = got_time.minute

exactly = "ровно"
half = "половина"
minute, few_minutes, minutes = "минута", "минуты", "минут"
hour, few_hours, hours = "час", "часа", "часов"

dict_hours = {
    0: ("двенадцать", "первого"), 1: ("один", "второго"), 2: ("два", "третьего"), 3: ("три", "четвертого"),
    4: ("четыре", "пятого"), 5: ("пять", "шестого"), 6: ("шесть", "седьмого"), 7: ("семь", "восьмого"),
    8: ("восемь", "девятого"), 9: ("девять", "десятого"), 10: ("десять", "одиннадцатого"),
    11: ("одиннадцать", "двенадцатого"), 12: ("двенадцать", "первого")
}

dict_minutes = {
    1: ("одна", "одной"), 2: ("две", "двух"), 3: ("три", "трех"), 4: ("четыре", "четырех"), 5: ("пять", "пяти"),
    6: ("шесть", "шести"), 7: ("семь", "семи"), 8: ("восемь", "восьми"), 9: ("девять", "девяти"),
    10: ("десять", "десяти"), 11: ("одиннадцать", "одиннадцати"), 12: ("двенадцать", "двенадцати"),
    13: ("тринадцать", "тринадцати"), 14: ("четырнадцать", "четырнадцати"), 15: ("пятнадцать", "пятнадцати"),
    16: ("шестнадцать",), 17: ("семнадцать",), 18: ("восемнадцать",), 19: ("девятнадцать",), 20: ("двадцать",),
    30: "тридцать", 40: "сорок"
}

# min == 0: такое-то значение часа ровно
if got_min == 0:
    if got_hour == 1:
        print(f"{dict_hours[got_hour][0]} {hour} {exactly}")
    elif 1 < got_hour < 5:
        print(f"{dict_hours[got_hour][0]} {few_hours} {exactly}")
    else:
        print(f"{dict_hours[got_hour][0]} {hours} {exactly}")

# min < 30: столько-то минут следующего часа
elif got_min < 30:
    if got_min <= 20:
        if got_min == 1:
            print(f"{dict_minutes[got_min][0]} {minute} {dict_hours[got_hour][1]}")
        elif 1 < got_min < 5:
            print(f"{dict_minutes[got_min][0]} {few_minutes} {dict_hours[got_hour][1]}")
        else:
            print(f"{dict_minutes[got_min][0]} {minutes} {dict_hours[got_hour][1]}")
    else:
        if got_min == 21:
            print(f"{dict_minutes[20][0]} {dict_minutes[got_min - 20][0]} {minute} {dict_hours[got_hour][1]}")
        elif 21 < got_min < 25:
            print(f"{dict_minutes[20][0]} {dict_minutes[got_min - 20][0]} {few_minutes} {dict_hours[got_hour][1]}")
        else:
            print(f"{dict_minutes[20][0]} {dict_minutes[got_min - 20][0]} {minutes} {dict_hours[got_hour][1]}")

# min == 30: половина такого-то
elif got_min == 30:
    print(f"{half} {dict_hours[got_hour][1]}")

# min > 30 and min < 45 столько-то минут следующего часа
elif 30 < got_min < 45:
    if got_min == 40:
        print(f"{dict_minutes[got_min]} {minutes} {dict_hours[got_hour][1]}")
    else:
        if got_min == 41 or got_min == 31:
            print(f"{dict_minutes[got_min - 1]} {dict_minutes[1][0]} {minute} {dict_hours[got_hour][1]}")
        elif 41 < got_min < 45:
            print(f"{dict_minutes[40]} {dict_minutes[got_min - 40][0]} {few_minutes} {dict_hours[got_hour][1]}")
        else:
            if 31 < got_min < 35:
                print(f"{dict_minutes[30]} {dict_minutes[got_min - 30][0]} {few_minutes} {dict_hours[got_hour][1]}")
            else:
                print(f"{dict_minutes[30]} {dict_minutes[got_min - 30][0]} {minutes} {dict_hours[got_hour][1]}")

# min >= 45 без min такого-то
else:
    print(f"без {dict_minutes[60 - got_min][1]} {dict_hours[got_hour + 1][0]}")
