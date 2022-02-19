# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр
#  "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов как
# ограничения на длину строки, при этом если слово целиком не умещается в строке,
#  оно должно быть перенесено на следующую, а отступы между словами
#  равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

while True:
    elem = input('How many symbos might be in one line? (UserEnter > 35): ')
    if elem.isdigit():
        elem = int(elem)
        break
    else:
        print('You have entered wrong number, try again!')
        continue

def cutStr(line):
                if len(line) <= elem:
                    nf.write(line)
                    return 
                if line[elem] == ' ':
                    nf.write(line[0:elem]+'\n')
                    symForNlInOldStr = elem
                else:
                    amountOfSymbols = 0
                    for i in range(elem-1, 0, -1):
                        if line[i] == ' ':
                            break
                        amountOfSymbols += 1
                    symForNl = elem - amountOfSymbols-1
                    symForNlInOldStr = symForNl
                    it = 0
                    for ch in line:
                        if symForNl == it:
                            nf.write('\n')
                            break
                        nf.write(ch)
                        if ch == ' ' and amountOfSymbols != 0:
                            nf.write(' ')
                            amountOfSymbols -= 1
                            symForNl += 1
                            it += 1
                        it += 1
                cutStr(line[symForNlInOldStr+1:])

with open('text.txt', 'r') as f:
    with open('newText.txt', 'w+') as nf:
        print('New file was created successfully!')
        for line in f:
            cutStr(line)
