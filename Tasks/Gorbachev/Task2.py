import datetime

def number_to_words(h, m):     # convert number to words
    h_word = ["час", "часа", "часов"]
    m_word = ["минута", "минуты", "минут"]
    h_1 = {1: 'один', 2:'два', 3:'три' ,4:'четыре' ,5:'пять' ,6:'шесть' ,7:'семь',
            8:'восемь' ,9:'девять' ,10:'десять' ,11:'одинадцать' ,12:'двенадцать'}
    h_2_12 = {1:'второго' ,2:'третьего' ,3:'четвёртого' ,4:'пятого' ,5:'шестого' ,6:'седьмого',
            7:'восьмого' ,8:'девятого' ,9:'десятого' ,10:'одиннадцатого' ,11:'двенадцатого' ,12:'первого'}
    m_2_12 = {1: 'одной', 2: 'двух', 3: 'трех', 4: 'четырех', 5: 'пяти', 6: 'шести', 7: 'семи', 8: 'восьми', 9: 'девяти', 10: 'десяти',
         11: 'одиннадцати', 12: 'двенадцати', 13: 'тринадцати', 14: 'четырнадцати', 15: 'пятнадцати'}
    m_1 = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    m_2 = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят'}
    m_3 = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    if m == 0:
        h_r = h_word[0] if ((h == 1) or (h ==13)) else h_word[1] if (1 < h < 5) else h_word[2]
        print(f"{h_1[h].capitalize()} {h_r} ровно")
    if (0 < m < 30):
        if m < 10:
            m_r = m_word[0] if (m == 1) else m_word[1] if (1 < m < 5) else m_word[2]
            print (f"{m_1[m].capitalize()} {m_r} {h_2_12[h]}")
        elif 10 < m < 20:
            print (f"{m_3[m].capitalize()} {m_word[2]} {h_2_12[h]}")
        elif m >= 10 and m in m_2:
            print (f"{m_2[m].capitalize()} {m_word[2]} {h_2_12[h]}")
        else:
            div_1 = m % 10
            div_2 = m - div_1
            m_r = m_word[0] if (div_1 == 1) else m_word[1] if (1 < div_1 < 5) else m_word[2]
            print(f"{m_2[div_2].capitalize()} {m_1[div_1]} {m_r} {h_2_12[h]}") 
    if m == 30:
        print(f"Половина {h_2_12[h]}")   
    if (30 < m < 45):
        div_1 = m % 10
        div_2 = m - div_1
        m_r = m_word[0] if (div_1 == 1) else m_word[1] if (1 < div_1 < 5) else m_word[2]
        print(f"{m_2[div_2].capitalize()} {m_1[div_1]} {m_r} {h_2_12[h]}") 
    if (m >= 45):
        m = 60 - m
        m_r = m_word[1] if (m == 1) else m_word[2]
        print(f"Без {m_2_12[m]} {m_r} {h_1[(h+1)]}")        
 
def time_now():     # enter current time
    c_time = datetime.datetime.today().strftime("%H:%M")
    c_hour, c_minutes = c_time.split(":")
    number_to_words((int(c_hour) - 12), int(c_minutes)) 
 
def user_time():  # enter user time
    k = False
    while k == False:
        print(f"Please enter valid time in format HH:MM")
        u_time = input()
        u_hour, u_minutes = u_time.replace(" ", "").replace("-",":").replace("_",  ":").split(":")
        u_hour = int(u_hour) - 12
        u_minutes = int(u_minutes)
        if (0 <= u_hour) and (u_hour <= 12) and (0 <= u_minutes) and (u_minutes <= 60):
            k = True
    number_to_words(u_hour, u_minutes)

def input_val():        # choosing options between system and user time
    x = 0
    while (x != 1) and (x != 2):
        print(f"Please choose a variant:")
        print(f"Enter value 1 to get current time")
        print(f"Enter value 2 to enter your personal time")
        x = int(input())
    return(x)

if input_val() == 1:
    time_now()
else:
    user_time()
 