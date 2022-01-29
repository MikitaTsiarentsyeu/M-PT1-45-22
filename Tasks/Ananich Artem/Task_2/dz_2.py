import datetime


print('Input 1 if you want to input time from your keybord; Input 2 if you want to leave the idea of inputing current time to computer')
a = input() #Ввод пользователя определяющий какой способ он хочет использовать

sHour = ['час' ,'часа' ,'часов']
sMin = ['минута' ,'минуты' ,'минут']

slovH = {1:'один' ,2:'два', 3:'три' ,4:'четыре' ,5:'пять' ,6:'шесть' ,7:'семь',
    8:'восемь' ,9:'девять' ,10:'десять' ,11:'одинадцать' ,12:'двенадцать' ,13:'один',
    14:'два' ,15:'три' ,16:'четыре' ,17:'пять' ,18:'шесть',
    19:'семь' ,20:'восемь' ,21:'девять', 22:'десять', 23:'одиннадцать',
    00:'двенадцать'}

slovM = {1:'одна' ,2:'две', 3:'три' ,4:'четыре' ,5:'пять' ,6:'шесть' ,7:'семь',
    8:'восемь' ,9:'девять' ,10:'десять' ,11:'одинадцать' ,12:'двенадцать' ,13:'тринадцать',
    14:'четырнадцать' ,15:'пятнадцать' ,16:'шестнадцать' ,17:'семнадцать' ,18:'восемнадцать',
    19:'девятнадцать' ,20:'двадцать' ,21:'двадцать одна', 22:'двадцать две', 23:'двадцать три',
    24:'двадцать четыре' ,25:'двадцать пять' ,26:'двадцать шесть' ,27:'двадцать семь',28:'двадцать восемь',
    29:'двадцать девять' ,31:'тридцать одна' ,32:'тридцать две' ,33:'тридцать три' ,34:'тридцать четыре',
    35:'тридцать пять' ,36:'тридцать шесть' ,37:'тридцать семь',38:'тридцать восемь' ,39:'тридцать девять',
    40:'сорок' ,41:'сорок одна' ,42:'сорок две' ,43:'сорок три',44:'сорок четыре'}

slovH12 = {1:'второго' ,2:'третьего' ,3:'четвёртого' ,4:'пятого' ,5:'шестого' ,6:'седьмого',
    7:'восьмого' ,8:'девятого' ,9:'десятого' ,10:'одиннадцатого' ,11:'двенадцатого' ,12:'первого',
    13:'второго' ,14:'третьего' ,15:'четвёртого' ,16:'пятого' ,17:'шестого' ,18:'седьмого',
    19:'восьмого' ,20:'девятого' ,21:'десятого' ,22:'одиннадцатого' ,23:'двенадцатого' ,00:'первого'}

slovM12 = {45:'пятнадцати' ,46:'четырнадцати' ,47:'тринадцати' ,48:'двенадцати' ,49:'одиннадцати',
    50:'десяти' ,51:'девяти' ,52:'восьми' ,53:'семи' ,54:'шести' ,55:'пяти' ,56:'четырёх' ,57:'трёх',
    58:'двух' ,59:'одной'}

t3 = 'ровно' #Создание всех переменных и словарей 
             #(создавал несколько словарей чтоб вам, Никита, было удобнее читать мой код :) )

if (a == '2'):
    d2 = datetime.datetime.today() #Использование метода класса datetime для того 
    d2 = str(d2)                   #чтоб компьютер мог сам определить текущее время
    d2 = d2.split()
    d2 = d2[1].split(':')
    hou2 = int(d2[0])
    min2 = int(d2[1])
    hou22 = d2[0]
    min22 = d2[1]
    s2 = '{}:{}'.format(hou22,min22)
    print(s2) #Создание всех переменных, которые будут использоваться только в проверках условий и 
              #вывод на экран текущего значения временя в цифровом виде
    
    if (min2 == 00):
        if (hou2 == 1):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[0],t3).capitalize()
            print(s1)
        elif (hou2 > 1) and (hou2 < 5):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[1],t3).capitalize()
            print(s1)
        elif (hou2 >= 5) and (hou2 <= 12):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[2],t3).capitalize()
            print(s1)
        elif (hou2 == 13):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[0],t3).capitalize()
            print(s1)
        elif (hou2 > 13) and (hou2 < 17):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[1],t3).capitalize()
            print(s1)
        elif (hou2 >= 17) and (hou2 < 24):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[2],t3).capitalize()
            print(s1)
        elif (hou2 == 00):
            s1 = '{} {} {}'.format(slovH[hou2],sHour[2],t3).capitalize()
            print(s1)
    elif (min2 < 30) and (min2 > 0):
        if (min2 == 21) or (min2 == 1):
            s1 = '{} {} {}'.format(slovM[min2],sMin[0],slovH12[hou2]).capitalize() 
            print(s1)   
        elif ((min2 > 1) and (min2 < 5)) or ((min2 > 21) and (min2 < 25)):
            s1 = '{} {} {}'.format(slovM[min2],sMin[1],slovH12[hou2]).capitalize()
            print(s1)
        else:
            s1 = '{} {} {}'.format(slovM[min2],sMin[2],slovH12[hou2]).capitalize()
            print(s1)
    elif (min2 == 30):
        s1 = 'половина {}'.format(slovH12[hou2]).capitalize()
        print(s1)
    elif (min2 > 30) and (min2 < 45):
        if (min2 == 31) or (min2 == 41):
            s1 = '{} {} {}'.format(slovM[min2],sMin[0],slovH12[hou2]).capitalize()
            print(s1)
        elif ((min2 > 31) and (min2 < 35)) or ((min2 > 41) and (min2 < 45)):
            s1 = '{} {} {}'.format(slovM[min2],sMin[1],slovH12[hou2]).capitalize()
            print(s1)
        elif (min2 > 34) and (min2 < 41):
            s1 = '{} {} {}'.format(slovM[min2],sMin[2],slovH12[hou2]).capitalize()
            print(s1)
    elif (min2 >= 45) and (min2 < 60):
        s1 = 'без {} {} {}'.format(slovM12[min2],sMin[2],slovH12[hou2]).capitalize()
        print(s1)#Проверка всех условий и вывод на экран подходящего для нас значения
                    
elif (a == '1'):
    t1 = input('Input time, for example: 15:34  ')
    t1 = t1.split(':')
    hou1 = int(t1[0])
    min1 = int(t1[1])
    hou11 = t1[0]
    min11 = t1[1]
    t2 = '{}:{}'.format(hou11,min11) #Все то же самое что и для предыдущего случая
    
    print(t2)    
    
    if (min1 == 00):
        if (hou1 == 1):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[0],t3).capitalize()
            print(s1)
        elif (hou1 > 1) and (hou1 < 5):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[1],t3).capitalize()
            print(s1)
        elif (hou1 >= 5) and (hou1 <= 12):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[2],t3).capitalize()
            print(s1)
        elif (hou1 == 13):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[0],t3).capitalize()
            print(s1)
        elif (hou1 > 13) and (hou1 < 17):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[1],t3).capitalize()
            print(s1)
        elif (hou1 >= 17) and (hou1 < 24):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[2],t3).capitalize()
            print(s1)
        elif (hou1 == 00):
            s1 = '{} {} {}'.format(slovH[hou1],sHour[2],t3).capitalize()
            print(s1)
    elif (min1 < 30) and (min1 > 0):
        if (min1 == 21) or (min1 == 1):
            s1 = '{} {} {}'.format(slovM[min1],sMin[0],slovH12[hou1]).capitalize() 
            print(s1)   
        elif ((min1 > 1) and (min1 < 5)) or ((min1 > 21) and (min1 < 25)):
            s1 = '{} {} {}'.format(slovM[min1],sMin[1],slovH12[hou1]).capitalize()
            print(s1)
        else:
            s1 = '{} {} {}'.format(slovM[min1],sMin[2],slovH12[hou1]).capitalize()
            print(s1)
    elif (min1 == 30):
        s1 = 'половина {}'.format(slovH12[hou1]).capitalize()
        print(s1)
    elif (min1 > 30) and (min1 < 45):
        if (min1 == 31) or (min1 == 41):
            s1 = '{} {} {}'.format(slovM[min1],sMin[0],slovH12[hou1]).capitalize()
            print(s1)
        elif ((min1 > 31) and (min1 < 35)) or ((min1 > 41) and (min1 < 45)):
            s1 = '{} {} {}'.format(slovM[min1],sMin[1],slovH12[hou1]).capitalize()
            print(s1)
        elif (min1 > 34) and (min1 < 41):
            s1 = '{} {} {}'.format(slovM[min1],sMin[2],slovH12[hou1]).capitalize()
            print(s1)
    elif (min1 >= 45) and (min1 < 60):
        s1 = 'без {} {} {}'.format(slovM12[min1],sMin[2],slovH12[hou1]).capitalize()
        print(s1)

elif (a != '1') and (a != '2'):
    print('You have entered wrong number! Check the conditions one more time!') 
#Если у пользователя плохое зрение то напомним ему об этом 
# в случае выбора несуществующего способа работы программы