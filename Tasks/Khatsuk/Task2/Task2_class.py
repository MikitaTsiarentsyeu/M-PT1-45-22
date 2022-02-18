from datetime import datetime
class time_to_text:
    def __init__(self):
        #списки числительных для часов, для одного часа - просто час
        self.zero_teens_hours = ['двенадцать','час','два','три','четыре','пять','шесть','семь','восемь',
                        'девять','десять','одиннадцать']
        self.zero_teens_hours_ogo= ['двенадцатого','первого','второго','третьего','четвертого',
                        'пятого','шестого','седьмого','восьмого','девятого','десятого',
                        'одиннадцатого']
        #списки числительных для минут
        self.zero_teens_minutes = ['','одна','две','три','четыре','пять','шесть','семь','восемь',
                        'девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать',
                        'пятнадцать','шестнадцать','семнадцать', 'восемнадцать','девятнадцать']
        self.one_teens_minutes_bez = ['выравнивание','одной','двух','трех','четырех','пяти','шести','семи','восмьи',
                        'девяти','десяти','одиннадцати','двенадцати','тринадцати','четырнадцати',
                        'пятнадцати']
        #список числительных десятков
        self.dozens = ['', '', 'двадцать','тридцать','сорок']
        #списки для "час" и "минута" в разных падежах
        self.hours = ['часов', 'час','часа']
        self.minutes = ['минут', 'минута', 'минуты']
        #индекс в списке падежей для числительных
        self.padezh = [0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        #дополнительно генерируем для минут спискок числительных больше 19 и соответствующие падежи
        self.minutes_fullist = self.zero_teens_minutes
        for i in range(2, 5):
            for j in range(10):
                min = ' '.join([self.dozens[i],self.zero_teens_minutes[j]])
                self.minutes_fullist.append(min)
                self.padezh.append(self.padezh[j])

        #для каждого случая из условия задачи возвращаем функцию, генерирующую соответствующую строку
        self.func_dict = \
                {#                         hh                          часов                                   ровно, но 'час ровно'
                0: lambda h, m : '{} {} {}'.format(self.zero_teens_hours[h], self.hours[self.padezh[h]] if h!= 1 else '\b', 'ровно'),
                #                               mm                          минут                             (hh+1)-го
                1: lambda h, m : '{} {} {}'.format(self.minutes_fullist[m], self.minutes[self.padezh[m]], self.zero_teens_hours_ogo[(h+1)%12]),
                #                           половина        (hh +1)-го
                2: lambda h, m : '{} {}'.format('половина', self.zero_teens_hours_ogo[(h+1)%12]),
                #                           без         (60 -mm)             минут (hh +1),  но 'без одной минуты'
                3: lambda h, m : '{} {} {} {}'.format('без', self.one_teens_minutes_bez[60-m], 'минут' if m!= 59 else 'минуты',
                                               self.zero_teens_hours[(h+1)%12])
                }

    def __call__(self, hh:'часы', mm:'минуты'):
        hh, mm = hh % 12, mm % 60,
        #считаем ключ для словаря
        #проверяем в каком диапазоне значение минут
        time_index = (mm == 0, (0 < mm < 30) or (30 < mm < 45), mm == 30, mm >= 45)
        #переходим к ключу в виде числа - индексу ненулевого значения
        time_index = time_index.index(1)
        return self.func_dict[time_index](hh, mm)
text_time = time_to_text()
print("введите время в формате часы:минуты\nдругие символы для отображения текущего времени\nдля выхода введите пробел")
while True:
    input_time = input()
    #можно использовать исключения либо регулярные выражения, но мы испльзуем строковые методы
    if  (input_time.count(':') == 1 and input_time.replace(':','', 1).isdigit()) :
        [hh, mm] = input_time.split(':')
        print(text_time(int(hh), int(mm)))
    elif input_time.isspace():
        break
    else:
        what_time = datetime.today()
        print(f'текущее время: {text_time(what_time.hour, what_time.minute)}')

