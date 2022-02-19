# 1. Реализовать функцию check_str которая получает на вход непустую строку и 
# выдаёт информацию о количестве букв в верхнем и нижнем регистре.
#check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'

text = ('The quick Brow Fox')

def string_test(text):
    dict={"UP_case":0, "LOW_case":0}
    for c in text:
        if c.isupper():
          dict["UP_case"]+=1
        elif c.islower():
           dict["LOW_case"]+=1
        else:
           pass
    print (f"""\n '{dict["UP_case"]} upper case, {dict["LOW_case"]} lower case' \n""")
    
string_test(text)