while True:
    x = int(input("Максимальное количество символов в строке (не меньше 35): "))
    if x < 35:
        print("Вводимое значение недостаточно большое")
        continue
    break

with open("text_new_version.txt", "w", encoding = 'utf-8') as fw:
    with open("text.txt", "r", encoding = 'utf-8') as fr:
        line = fr.readlines()

    final_text = ""

    for z in line: #подсмотрела как разделить с сохранением переносов
        lines = z.split()

        sum_elem = 0
        text = ""
        
        for i in lines:
            sum_elem += len(i) + 1
            if sum_elem < x:
                text += i + " "
            if sum_elem == x:
                text += i
                text += "\n"
                final_text += text
                text, sum_elem = "", 0
            if sum_elem > x:
                text = text[:-1]
                while len(text) != x: #и это я подсмотрела (мне не особо стыдно, к счастью или сожалению)
                    spaces = x - len(text)
                    text = text.replace(' ', '  ', spaces)
                text += "\n"
                final_text += text
                text, sum_elem = i + " ", len(i) + 1,

        final_text += text + "\n"
    fw.write(final_text) 

print(f"Ваш новый текст с {x} символами в строке в файле: text_new_version.txt")
