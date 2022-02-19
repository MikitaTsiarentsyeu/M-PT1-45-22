# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)


while True:
    max = input("Enter the maximum number of characters per line (more than 35). ")
    if not max.isdigit():
        print ("Enter the number.")
        continue
    max = int(max)
    if max <= 35:
        print ("Please enter a higher number.")
        continue
    break

with open('Tasks\\Machekhin_Vlad\\Task4\\text.txt', 'r', encoding="utf8") as f: # yes yes, absolute links
    with open('Tasks\\Machekhin_Vlad\\Task4\\testik.txt', 'w', encoding='utf-8') as kekus:
        for stroka in f:
            words = stroka.split()
            num_elem = 0
            space = 0
            res = ''

            for word in words: #word counter
                num_elem += len(word) + 1 

                if num_elem-1 > max:
                    res = res[:-1] # cut off the last space
                    
                    while len(res) != max: # adding spaces
                        difference_mr = max - len(res) # counting the required number of spaces
                        if difference_mr > space:
                            difference_mr = space
                        res = res.replace(' ', '  ', difference_mr)
                    print (res)
                    
                    kekus.write(res + '\n') # writing text
                    
                    res = word + " "
                    space = 1
                    num_elem = len(res)
                    continue

                res += word + " "
                space += 1
            print(res)
            kekus.write(res + '\n')

        print ("This terrible task is complete. The new file has been written.")
            
             

