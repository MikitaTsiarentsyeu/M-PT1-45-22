# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'

def chek_str(inp_str):
    print(inp_str)
    inp_str_rep = inp_str.replace(" ","") # минус пробелы для адекватной разбивки по буквам
    l = 0
    u = 0
    for i in inp_str_rep: #по буквам
        if i.islower():
            l += 1
        else:
            u += 1
    print(f"{u} upper case,{l} lower case")

chek_str("The quick Brow Fox")
