"""1. Прочитать содержимое файла text.txt
2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую,
а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
(модуль textwrap использовать нельзя)"""


def read_func():
    with open("text.txt", 'r', encoding="utf-8") as f:
        text = f.readlines()
    f.close()
    return(text)

def input_func():
    while True:
        symbol_num = input("Please enter maximum number of elements in a line (it must be number bigger than 35)...\n")
        if not symbol_num.isdigit():
            print("Input is incorrect! Please enter a number!")
            continue 
        if int(symbol_num) <= 35:
            print("Input is incorrect! Please enter a number bigger than 35!")
            continue            
        break  
    return(int(symbol_num))

def format_func(num, text_raw):
    text_output = ""
    for line in text_raw:
        words_sep = line.split()
        line_length = 0
        text_format = "" # formatted text consisting of line_format (already limited lines)
        line_format = "" # line limited by number of symbols
        for word in words_sep:
            line_length += (len(word) + 1) 
            if line_length-1 > num: 
                line_format = line_format[:-1]
                len(line_format)
                while len(line_format) < num:
                    diff = num - len(line_format)
                    line_format = line_format.replace(' ', '  ', diff)
                text_format += line_format + "\n" # adding formatted line to the formatted text
                line_length = (len(word) + 1) # length of the current word goes to next step
                line_format = ""
            line_format += (word + " ") # creating line of separated words
        text_format += line_format + "\n" # adding formatted line to the formatted text
        text_output += text_format
    return(text_output)

def write_func(num, text_output):
    with open("output.txt", 'w', encoding="utf-8") as f:
        f.write(text_output)
    f.close()
    print(f"Dear User your text were formatted corresponding to the lenght of the line - {num} symbols."+"\n"+"Output.txt file were created!")
        
        
num = input_func()       
text_raw = read_func()
text_output = format_func(num, text_raw)
write_func(num, text_output)