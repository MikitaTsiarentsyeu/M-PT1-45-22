# Задание:

# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не
# умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией
# "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя. (модуль textwrap использовать нельзя)

# ------------------------------------------------------------------------------------------------------------------ #

# Решение: N_1:

# user interaction
width = 0
while width < 36:
    try:
        width = int(input("please enter your text`s width > 35 | "))
    except:
        print("your enter are not correct, please try again")
# text formatting
with open("file.txt") as f, open("new_file.txt", "w") as new_f:
    text = f.read().split()
    line = []
    for word in text:
        if width - len("".join(line)) >= len(word):
            line.append(word), line.append(" ")
        else:
            line.pop()
            while len("".join(line).rstrip()) != width:
                for i_d, symbol in enumerate(line):
                    if len("".join(line).rstrip()) == width:
                        break
                    if symbol != " ":
                        line.insert(i_d + 1, " ")
            new_f.write("".join(line) + "\n")
            line = [word, " "]
    new_f.write("".join(line)), f.close(), new_f.close()
print(f"your text with a width of {width} symbol is formatted and written to a file called 'new_file'")

# ------------------------------------------------------------------------------------------------------------------ #

# Решение: N_2: 

from func import add_gaps, write_file

# user interaction
width = 0
while width < 36:
    try:
        width = int(input("please enter your text`s width > 35 | "))
    except:
        print("your enter are not correct, please try again")
# text formatting
with open("file.txt") as f, open("new_file_2.txt", "w") as new_f:
    for line_file in f:
        text = line_file.strip().split()
        line = []
        for word in text:
            if width - len("".join(line)) >= len(word):
                line.append(word), line.append(" ")
            else:
                add_gaps(width, line)
                write_file(new_f, line)
                line = [word, " "]
        add_gaps(width, line)
        write_file(new_f, line)
print(f"your text with a width of {width} symbol is formatted and written to a file called 'new_file'")
