from datetime import datetime
def time_to_text(hh:'часы', mm:'минуты'):
    "текстовое представление времени"
    #списки числительных для часов, для одного часа - просто час
    zero_teens_hours = ['двенадцать','час','два','три','четыре','пять','шесть','семь','восемь',
                    'девять','десять','одиннадцать']
    zero_teens_hours_ogo= ['двенадцатого','первого','второго','третьего','четвертого',
                    'пятого','шестого','седьмого','восьмого','девятого','десятого',
                    'одиннадцатого']
    #списки числительных для минут
    zero_teens_minutes = ['','одна','две','три','четыре','пять','шесть','семь','восемь',
                    'девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать',
                    'пятнадцать','шестнадцать','семнадцать', 'восемнадцать','девятнадцать']
    one_teens_minutes_bez = ['выравнивание','одной','двух','трех','четырех','пяти','шести','семи','восмьи',
                    'девяти','десяти','одиннадцати','двенадцати','тринадцати','четырнадцати',
                    'пятнадцати']
    #список числительных десятков
    dozens = ['', '', 'двадцать','тридцать','сорок']
    #списки для "час" и "минута" в разных падежах
    hours = ['часов', 'час','часа']
    minutes = ['минут', 'минута', 'минуты']
    #индекс в списке падежей для числительных
    padezh = [0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #дополнительно генерируем для минут спискок числительных больше 19 и соответствующие падежи
    minutes_fullist = zero_teens_minutes
    for i in range(2, 5):
        for j in range(10):
            min = ' '.join([dozens[i],zero_teens_minutes[j]])
            minutes_fullist.append(min)
            padezh.append(padezh[j])

    #для каждого случая из условия задачи возвращаем функцию, генерирующую соответствующую строку
    func_dict = { 0: lambda h, m : '{} {} {}'.format(zero_teens_hours[h], hours[padezh[h]] if h!= 1 else '\b', 'ровно'),#'hh часов', но 'час ровно'
                1: lambda h, m : '{} {} {}'.format(minutes_fullist[m], minutes[padezh[m]], zero_teens_hours_ogo[(h+1)%12]),
                2: lambda h, m : '{} {}'.format('половина', zero_teens_hours_ogo[(h+1)%12]),
                3: lambda h, m : '{} {} {} {}'.format('без', one_teens_minutes_bez[60-m], 'минут' if m!= 59 else 'минуты',
                                           zero_teens_hours[(h+1)%12])#'без mm минут', но 'без одной
                }
    hh, mm = hh % 12, mm % 60,
    #считаем ключ для словаря
    #проверяем в каком диапазоне значение минут
    time_index = (mm == 0, (0 < mm < 30) or (30 < mm < 45), mm == 30, mm >= 45)
    #переходим к ключу в виде числа - индексу ненулевого значения
    time_index = time_index.index(1)
    return func_dict[time_index](hh, mm)
print("введите время в формате часы:минуты\nдругие символы для отображения текущего времени\nдля выхода введите пробел")
while True:
    input_time = input()
    #можно использовать исключения либо регулярные выражения, но мы испльзуем строковые методы
    if  (input_time.count(':') == 1 and input_time.replace(':','', 1).isdigit()) :
        [hh, mm] = input_time.split(':')
        print(time_to_text(int(hh), int(mm)))
    elif input_time.isspace():
        break
    else :
        what_time = datetime.today()
        print(f'текущее время: {time_to_text(what_time.hour, what_time.minute)}')

