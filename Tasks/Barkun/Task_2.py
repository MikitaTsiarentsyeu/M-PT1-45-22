#            УСЛОВИЕ ЗАДАЧИ
#
#             Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого с консоли (hh:mm).
# (дать пользователю возможность выбрать режим работы программы)
# 
# Для получения текущего времени использовать модуль datetime.
# 
# min == 0: такое-то значение часа ровно
# min < 30: столько-то минут следующего часа
# min == 30: половина такого-то
# min > 30 and min < 45 столько-то минут следующего часа
# min >= 45 без min такого-то
#
# 21:16
# шестнадцать минут десятого

#       РЕШЕНИЕ

from datetime import datetime
from tkinter import N

print ("\n\nПривет человек!")

valid_input = False
entered_time_hours_hh = 0
entered_time_min_mm = 0

while valid_input == False:                                    
    
    print ("\nЕсли ты хочешь получить текущее время, введи цифру  - 1\nЕсли ты живешь по своему времени, введи цифру       - 2")
    choose_time = input ("\nВведи ниже цифры 1 или 2\n")

    if choose_time == "1":
        current_time = datetime.today().strftime("%H:%M")
        print ("\nТекущее время:", "\n\n", current_time)
        
        entered_time = current_time    

        entered_time_hours_1 = int (entered_time [0])
        entered_time_hours_2 = int (entered_time [1])
        entered_time_min_1 = int (entered_time [3])
        entered_time_min_2 = int (entered_time [4])

        entered_time_hours_hh = entered_time_hours_1 * 10 + entered_time_hours_2

        entered_time_min_mm = entered_time_min_1 * 10 + entered_time_min_2    

        valid_input = True

    elif choose_time != "1" and choose_time != "2":
        print ("Вы ввели - " + choose_time + ". Это неверный ввод. Повторите пожалуйста.")   
    
    elif choose_time == "2":
        user_time = input ("""\nВведите ниже время в любом удобном Вам формате "ЧЧ:MM", "ЧЧ-MM", "ЧЧ_MM ..."\n""" )
        entered_time = user_time
   
#                           Проверяем на правильность ввода времени                             

        try:
            entered_time_hours_1 = int (entered_time [0])
            entered_time_hours_2 = int (entered_time [1])
            entered_time_min_1 = int (entered_time [3])
            entered_time_min_2 = int (entered_time [4])

            entered_time_hours_hh = entered_time_hours_1 * 10 + entered_time_hours_2

            entered_time_min_mm = entered_time_min_1 * 10 + entered_time_min_2    

            if (entered_time_hours_hh > 24 or entered_time_hours_hh < 0) or (
                entered_time_min_mm > 59 or entered_time_min_mm < 0) or len(entered_time) != 5:
                print ("\nНеверный ввод")
                print ('\nВы живете не на планете Земля?!\n', """\nЕсли все-таки на "Земле", то повторите ввод\n""", 
                '\nНапоминаю, что на планете Земля, в сутках - 24 часа, а в часe - 60 минут.')
                valid_input = False
            else:
                valid_input = True
        except Exception:
                print ("\nНеверный ввод времени")
                valid_input = False
                
dict_time_hh = {0 : 'ноль', 1 : 'один', 111: 'час', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять', 6 : 'шесть', 
7 : 'семь', 8 : 'восемь', 9 : 'девять', 10 : 'десять', 11 : 'одинадцать', 12 : 'двенадцать', 13 : 'первого', 
14 : 'второго', 15 : 'третьего', 16 : 'четвертого', 17 : 'пятого', 18 : 'шестого', 19 : 'седьмого', 20 : 'восьмого', 
21 : 'девятого', 22 : 'десятого', 23 : 'одинадцатого', 24 : 'двенадцатого', 25: 'первого',}

dict_time_hh_text = {0 : 'часов', 1: 'час', 2: 'часа', 3 : 'ровно',}   

dict_time_mm = {1 : 'одна', 2 :'две', 3 :'три', 4:'четыре', 5 :'пять', 6 :'шесть', 7 :'семь', 8 :'восемь', 9 :'девять', 10 :'десять', 
11 :'одинадцать', 12 :'двенадцать', 13 :'тринадцать', 14 :'четырнадцать', 15 :'пятнадцать', 16 :'шестнадцать', 17 :'семнадцать', 
18 :'восемнадцать', 19 :'девятнадцать', 20 : 'двадцать', 21 :'двадцать одна', 22 : 'двадцать две', 23 : 'двадцать три', 
24 : 'двадцать четыре', 25 : 'двадцать пять', 26 : 'двадцать шесть', 27 : 'двадцать семь', 28 : 'двадцать восемь', 
29 : 'двадцать девять', 30 : 'половина', 31: 'тридцать одна', 32 :'тридцать две', 33 : 'тридцать три', 34 : 'тридцать четыре',
35 : 'тридцать пять', 36 : 'тридцать шесть', 37 : 'тридцать семь', 38 : 'тридцать восемь', 39 : 'тридцать девять', 
40 :'сорок', 41 : 'сорок одна', 42 :'сорок две', 43 : 'сорок три', 44 : 'сорок четыре', 45 : 'без пятнадцати', 46 : 'без четырнадцати',
47 : 'без тринадцати', 48 : 'без двенадцати', 49 : 'без одинадцати', 50 : 'без десяти', 51 : 'без девяти', 52 : 'без восьми', 
53 :'без семи', 54 : 'без шести', 55 : 'без пяти', 56 : 'без четырех', 57 : 'без трех', 58 : 'без двух', 59 : 'без одной',}

dict_time_mm_text = {1 : 'минута', 2: 'минуты', 3: 'минут',}  

if entered_time_hours_hh >= 13:
    entered_time_hours_hh = entered_time_hours_hh - 12     # приводим к 12 часовому формату
    
#                            Разбираемся с вариантами часов

#           часов ровно

if (entered_time_hours_hh == 0 or entered_time_hours_hh  >= 5) and (entered_time_hours_hh <= 12 and entered_time_min_mm == 0):
    text_hour = dict_time_hh [entered_time_hours_hh]
    text_hour_text = dict_time_hh_text [0]
    text_hour_text_evenly = dict_time_hh_text [3]

#           часа ровно

elif 2 <= entered_time_hours_hh <= 4:
    text_hour = dict_time_hh [entered_time_hours_hh]
    text_hour_text = dict_time_hh_text [2]
    text_hour_text_evenly = dict_time_hh_text [3]

#           час ровно

else: #entered_time_hours_hh == 1
    text_hour = dict_time_hh [entered_time_hours_hh]
    text_hour_text = dict_time_hh_text [1]
    text_hour_text_evenly = dict_time_hh_text [3]
    
    #                            Разбираемся с минутами

    #       минута

if (entered_time_min_mm == 1 or entered_time_min_mm == 21) or (entered_time_min_mm == 31 or entered_time_min_mm == 41):
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [1]
    text_min_text_evenly = dict_time_hh [entered_time_hours_hh + 13]

    #       минуты

elif 2 <= entered_time_min_mm <= 5 or 22 <= entered_time_min_mm <= 24 or 32 <= entered_time_min_mm <= 34 or 42 <= entered_time_min_mm <= 44:
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [2]
    text_min_text_evenly = dict_time_hh[entered_time_hours_hh + 13]

#           минут

elif 6 <= entered_time_min_mm <=20 or 25 <= entered_time_min_mm <= 29 or 35 <= entered_time_min_mm <= 40:
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [3]
    text_min_text_evenly = dict_time_hh [entered_time_hours_hh + 13]

#           Половина

elif entered_time_min_mm == 30:
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm [30]
    text_min_text_evenly = dict_time_hh [entered_time_hours_hh + 13]

#           Без .... минут

elif 45 <= entered_time_min_mm <= 58 and entered_time_hours_hh != 0: 
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [3]
    text_min_text_evenly = dict_time_hh [entered_time_hours_hh + 1]

#           Без одной минуты

elif entered_time_min_mm == 59 and  entered_time_hours_hh > 0:  
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [2]
    text_min_text_evenly = dict_time_hh [entered_time_hours_hh + 1]

#           Без одной минуты час

elif entered_time_min_mm == 59 and  entered_time_hours_hh == 0:  
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [2]
    text_min_text_evenly = dict_time_hh [111]

#           Без ... минут час

elif 45 <= entered_time_min_mm <= 58 and  entered_time_hours_hh == 0:
    text_min = dict_time_mm [entered_time_min_mm]
    text_min_text = dict_time_mm_text [3]
    text_min_text_evenly =  dict_time_hh [111]

#                               выводы

if entered_time_min_mm == 0:
    print ("\n", text_hour.capitalize(), text_hour_text, text_hour_text_evenly) 

elif entered_time_min_mm == 30:
    print ("\n", text_min_text.capitalize(), text_min_text_evenly) 

elif entered_time_min_mm >=45: #and entered_time_min_mm <= 59:
    print ("\n", text_min.capitalize(), text_min_text, text_min_text_evenly)   

else: 
    print ("\n", text_min.capitalize(), text_min_text, text_min_text_evenly)

print ('\nВыполнение программы закончено!\n\nСпасибо\n')
