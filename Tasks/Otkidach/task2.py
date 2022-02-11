#представим, что пользователь образованный человек и ему не придет в голову вкидывать всякую ерунду в инпут кроме [часы:минуты]
#хотя чисто в теории, в будущем можно дописать сюда цикл, который пропускал бы только числовой нужный нам формат, но это не точно, надо подумать на досуге...

import datetime

hours = {1:'один' ,2:'два', 3:'три' ,4:'четыре' ,5:'пять' ,6:'шесть' ,7:'семь',
    8:'восемь' ,9:'девять' ,10:'десять' ,11:'одинадцать' ,12:'двенадцать' ,13:'один',
    14:'два' ,15:'три' ,16:'четыре' ,17:'пять' ,18:'шесть',
    19:'семь' ,20:'восемь' ,21:'девять', 22:'десять', 23:'одиннадцать',
    00:'двенадцать'}

hours2 = {1:'второго' ,2:'третьего' ,3:'четвёртого' ,4:'пятого' ,5:'шестого' ,6:'седьмого',
    7:'восьмого' ,8:'девятого' ,9:'десятого' ,10:'одиннадцатого' ,11:'двенадцатого' ,12:'первого',
    13:'второго' ,14:'третьего' ,15:'четвёртого' ,16:'пятого' ,17:'шестого' ,18:'седьмого',
    19:'восьмого' ,20:'девятого' ,21:'десятого' ,22:'одиннадцатого' ,23:'двенадцатого' ,00:'первого'}

no_minutes = 'ровно'

minutes = {1:'одна' ,2:'две', 3:'три' ,4:'четыре' ,5:'пять' ,6:'шесть' ,7:'семь',
    8:'восемь' ,9:'девять' ,10:'десять' ,11:'одинадцать' ,12:'двенадцать' ,13:'тринадцать',
    14:'четырнадцать' ,15:'пятнадцать' ,16:'шестнадцать' ,17:'семнадцать' ,18:'восемнадцать',
    19:'девятнадцать' ,20:'двадцать' ,21:'двадцать одна', 22:'двадцать две', 23:'двадцать три',
    24:'двадцать четыре' ,25:'двадцать пять' ,26:'двадцать шесть' ,27:'двадцать семь',28:'двадцать восемь',
    29:'двадцать девять' ,31:'тридцать одна' ,32:'тридцать две' ,33:'тридцать три' ,34:'тридцать четыре',
    35:'тридцать пять' ,36:'тридцать шесть' ,37:'тридцать семь',38:'тридцать восемь' ,39:'тридцать девять',
    40:'сорок' ,41:'сорок одна' ,42:'сорок две' ,43:'сорок три',44:'сорок четыре'}

minutes2 = {45:'пятнадцати' ,46:'четырнадцати' ,47:'тринадцати' ,48:'двенадцати' ,49:'одиннадцати',
    50:'десяти' ,51:'девяти' ,52:'восьми' ,53:'семи' ,54:'шести' ,55:'пяти' ,56:'четырёх' ,57:'трёх',
    58:'двух' ,59:'одной'}

time = input('Введите время в формате [часы:минуты]: ') #если вводит пользователь
time = time.split(':')
hour_inp = int(time[0])
min_inp = int(time[1])

hour_input = time[0]
min_input = time[1]
time_out = '{}:{}'.format(hour_input,min_input)
print(time_out)    

hour_text = ['час' ,'часа' ,'часов']
minutes_text = ['минута' ,'минуты' ,'минут']

if (min_inp == 00):
    if (hour_inp == 1):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[0],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp > 1) and (hour_inp < 5):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[1],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp >= 5) and (hour_inp <= 12):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[2],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp == 13):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[0],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp > 13) and (hour_inp < 17):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[1],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp >= 17) and (hour_inp < 24):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[2],no_minutes).capitalize()
        print(time_out)
    elif (hour_inp == 00):
        time_out = '{} {} {}'.format(hours[hour_inp],hour_text[2],no_minutes).capitalize()
        print(time_out)
elif (min_inp < 30) and (min_inp > 0):
    if (min_inp == 21) or (min_inp == 1):
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[0],hours2[hour_inp]).capitalize() 
        print(time_out)   
    elif ((min_inp > 1) and (min_inp < 5)) or ((min_inp > 21) and (min_inp < 25)):
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[1],hours2[hour_inp]).capitalize()
        print(time_out)
    else:
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[2],hours2[hour_inp]).capitalize()
        print(time_out)
elif (min_inp == 30):
    time_out = 'половина {}'.format(hours2[hour_inp]).capitalize()
    print(time_out)
elif (min_inp > 30) and (min_inp < 45):
    if (min_inp == 31) or (min_inp == 41):
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[0],hours2[hour_inp]).capitalize()
        print(time_out)
    elif ((min_inp > 31) and (min_inp < 35)) or ((min_inp > 41) and (min_inp < 45)):
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[1],hours2[hour_inp]).capitalize()
        print(time_out)
    elif (min_inp > 34) and (min_inp < 41):
        time_out = '{} {} {}'.format(minutes[min_inp],minutes_text[2],hours2[hour_inp]).capitalize()
        print(time_out)
elif (min_inp >= 45) and (min_inp < 60):
    time_out = 'без {} {} {}'.format(minutes2[min_inp],minutes_text[2],hours2[hour_inp]).capitalize()
    print(time_out)

date_today = datetime.datetime.today() #если берем текущее время
date_today = str(date_today)                   
date_today = date_today.split()
date_today = date_today[1].split(':')
date_today_hour = int(date_today[0])
date_today_minutes = int(date_today[1])

date_today_hour_auto = date_today[0]
date_today_min_auto = date_today[1]
time_out_auto = '{}:{}'.format(date_today_hour_auto,date_today_min_auto)
print(time_out_auto)


if (date_today_minutes == 00):
    if (date_today_hour == 1):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[0],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour > 1) and (date_today_hour < 5):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[1],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour >= 5) and (date_today_hour <= 12):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[2],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour == 13):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[0],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour > 13) and (date_today_hour < 17):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[1],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour >= 17) and (date_today_hour < 24):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[2],no_minutes).capitalize()
        print(time_out)
    elif (date_today_hour == 00):
        time_out = '{} {} {}'.format(hours[date_today_hour],hour_text[2],no_minutes).capitalize()
        print(time_out)
elif (date_today_minutes < 30) and (date_today_minutes > 0):
    if (date_today_minutes == 21) or (date_today_minutes == 1):
        time_out = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[0],hours2[date_today_hour]).capitalize() 
        print(time_out)   
    elif ((date_today_minutes > 1) and (date_today_minutes < 5)) or ((date_today_minutes > 21) and (date_today_minutes < 25)):
        time_out = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[1],hours2[date_today_hour]).capitalize()
        print(time_out)
    else:
        time_out = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[2],hours2[date_today_hour]).capitalize()
        print(time_out)
elif (date_today_minutes == 30):
    time_out = 'половина {}'.format(hours2[date_today_hour]).capitalize()
    print(time_out)
elif (date_today_minutes > 30) and (date_today_minutes < 45):
    if (date_today_minutes == 31) or (date_today_minutes == 41):
        time_out = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[0],hours2[date_today_hour]).capitalize()
        print(time_out)
    elif ((date_today_minutes > 31) and (date_today_minutes < 35)) or ((date_today_minutes > 41) and (date_today_minutes < 45)):
        time_out = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[1],hours2[date_today_hour]).capitalize()
        print(time_out)
    elif (date_today_minutes > 34) and (date_today_minutes < 41):
        time_out_atime_oututo = '{} {} {}'.format(minutes[date_today_minutes],minutes_text[2],hours2[date_today_hour]).capitalize()
        print(time_out)
elif (date_today_minutes >= 45) and (date_today_minutes < 60):
    time_out = 'без {} {} {}'.format(minutes2[date_today_minutes],minutes_text[2],hours2[hour_inp]).capitalize()
    print(time_out)
