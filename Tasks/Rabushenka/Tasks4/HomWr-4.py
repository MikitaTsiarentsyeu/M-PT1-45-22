with open("text.txt", 'r', encoding='utf-8') as f:
    text = ''
    for string in f:
        text += string.replace('\n', '')
while True:
    question = input('Will display number of characters per "line minimum 35": ')
    if question.isdigit():
        question = int(question)
        if question < 35:
            print("Error. not less ( < 35).")
            continue
        else:
            break
    else:
        print("Error. Please enter numbers.")
        continue

list_of_words = text.split()
new_txt = ""
string_for_print = ""
length_string = 0
for i in range(len(list_of_words) - 1):
    if (len(string_for_print) + len(list_of_words[i])) < question:
        string_for_print += list_of_words[i] + ' '
        if (len(string_for_print) + len(list_of_words[i-1])) > question:
            string_for_print = string_for_print[:-1]
            while len(string_for_print) != question:
                spaces = question - len(string_for_print)
                string_for_print = string_for_print.replace(' ', '  ', spaces)
            else:
                print(string_for_print)
                string_for_print = ""
new_txt += string_for_print

with open("new.txt", "w", encoding='utf-8') as f:
    f.write(new_txt)