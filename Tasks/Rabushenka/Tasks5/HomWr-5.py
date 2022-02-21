# Еxercise 1
from math import sqrt
question = input("Input: ")
def string_symbols(string):
    dictionary = {"Upper case": 0, "Lower case": 0}
    for symbols in string:
        if symbols.isupper():
           dictionary["Upper case"]+=1
        elif symbols.islower():
           dictionary["Lower case"]+=1
        else:
           continue
    print ("Original String : ", string)
    print ("Upper case characters : ", dictionary["Upper case"])
    print ("Lower case Characters : ", dictionary["Lower case"])
string_symbols(question)

# Еxercise 2

question_2 = int(input("Input: "))
def string_symbols(number):
    if number < 2:
        return False
    if number == 2:
        return True
    limit = sqrt(number)
    check = 2
    while check <= limit:
        if number % check == 0:
            return False
        check += 1
    return True
if string_symbols(question_2) == True:
    print(question_2, "Prime number -",string_symbols(question_2))
if string_symbols(question_2) == False:
    print(question_2, "Сomplex number -",string_symbols(question_2))

# Еxercise 3
def sorting(string):
    new_list = []
    for i in range(len(string)- 1):
        if string[i] + 1 == string[i + 1]:
            if string[i] - 1 == string[i - 1]:
                continue
            else:
                new_list.append(str(string[i]))
                new_list.append("-")
        else:
            new_list.append(f'{(string[i])}{", "}')
    new_list.append(str(string[-1]))
    return "".join(new_list)
print(sorting([0, 1, 2, 3, 4, 7, 8, 10]))
print(sorting([4, 7, 10]))
print(sorting([2, 3, 8, 9]))
