# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

# Get some data from user
while True:
    elem_on_line = input("Input maximum number of characters per line (>35): ")

    if not elem_on_line.isdigit():
        print ("Input number pls!")
        continue

    elem_on_line = int(elem_on_line)
    if elem_on_line <= 35:
        print ("Input number which greater than 35")
        continue
    
    break

with open('text.txt', 'r', encoding='utf-8') as f:
    with open('test.txt', 'w', encoding='utf-8') as new_f:
        # Step by line to save paragraphs
        for line in f:
            words = line.split()
            output = ''
            sum_elem = 0
            count_space = 0
            
            # count how many words fit
            for word in words:
                # +1 to count space
                sum_elem += len(word) + 1 
                
                if sum_elem-1 > elem_on_line:
                    # delete last space
                    output = output[:-1] 
                    # add space between words
                    while len(output) != elem_on_line:
                        # Count how many spaces we should be added
                        difference = elem_on_line - len(output)
                        if difference > count_space:
                            difference = count_space
                        output = output.replace(' ', '  ', difference)
                    print (f'{output} - {len(output)}')
                    # write in file
                    new_f.write(output + '\n')
                    # Update counters
                    output = word + " "
                    count_space = 1
                    sum_elem = len(output)
                    continue

                output += word + " "
                count_space += 1
            # Add paragraph in files
            output = output[:-1]
            print (f'{output} - {len(output)}') # last line in paragraph
            new_f.write(output + '\n')

        print ("Your version text.txt in test.txt :D")