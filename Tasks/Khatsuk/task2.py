import datetime
def time_to_text(hh, mm):
    zero_teens_hours = ['двенадцать','один','два','три','четыре','пять','шесть','семь','восемь',
                    'девять','десять','одиннадцать']
    zero_teens_hours_ogo= ['двенадцатого','первого','второго','третьего','четвертого',
                    'пятого','шестого','седьмого','восьмого','девятого','десятого',
                    'одиннадцатого']
    zero_teens_minutes = ['','одна','две','три','четыре','пять','шесть','семь','восемь',
                    'девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать',
                    'пятнадцать','шестнадцать','семнадцать', 'восемнадцать','девятнадцать']
    one_teens_minutes_bez = ['выравнивание','одной','двух','трех','четырех','пяти','шести','семи','восмьи',
                    'девяти','десяти','одиннадцати','двенадцати','тринадцати','четырнадцати',
                    'пятнадцати']
    dozens = ['', '', 'двадцать','тридцать','сорок','пятьдесят']

    hours = ['часов', 'час','часа']
    minutes = ['минут', 'минута', 'минуты']
    padezh = [0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    minutes_fullist = zero_teens_minutes
    for i in range(2, 5):
        for j in range(10):
            min = ' '.join([dozens[i],zero_teens_minutes[j]])
            minutes_fullist.append(min)
            padezh.append(padezh[j])

    func_dict = { 0: lambda h, m : ' '.join([zero_teens_hours[h], hours[padezh[h]], 'ровно']),
                1: lambda h, m : ' '.join([minutes_fullist[m], minutes[padezh[m]], zero_teens_hours_ogo[(h+1)%12]]),
                2: lambda h, m : ' '.join([ 'половина', zero_teens_hours_ogo[(h+1)%12]]),
                3: lambda h, m : ' '.join(['без', one_teens_minutes_bez[60-m], 'минут' if m!= 59 else 'минуты',
                                           zero_teens_hours[(h+1)%12]])
                }

    hh, mm = hh % 12, mm % 60,
    time_index = (mm == 0, (0 < mm < 30) or (30 < mm < 45), mm == 30, mm >= 45)
    time_index = time_index.index(1)
    return func_dict[time_index](hh, mm)


what_time = datetime.datetime.today()
print(f'текущее время: {time_to_text(what_time.hour, what_time.minute)}')

while True:
    input_time = input('введите время в формате часы:инуты ')

    [hh, mm] = input_time.split(':')
    print(time_to_text(int(hh), int(mm)))
