def input_len(minlen=15):
    'ввод пользователем ширины текста - длина строк'
    while True:
        value = input('input line length more than 35:')
        if value.isdigit():
            value = int(value)
            if value >= minlen:
                return value

def line_fit(line_string, line_len):
    'форматирует строку до нужной длины'
    line_string = line_string.strip()
    space_number = line_string.count(' ')
    #высчитываем, сколько пробелов добавить
    addition_len = line_len - len(line_string)
    if not space_number or addition_len == 0:
        return line_string
    # высчитываем, сколько пробелов добавить к каждому имеющемуся x - результат целочисленнного деления
    #остаток y - количество пробелов, которые добавляем дополнительно
    x, y = divmod(addition_len, space_number)
    #к каждому пробелу добавляем x пробелов
    line_string = line_string.replace(' ', ' '*(x+1))
    #к первым y пробелам добавляем еще по пробелу
    line_string = line_string.replace(' '*(x+1), ' '*(x+2), y)
    return line_string
def line_extraction(input_string):
    "извлекает из строки подстроки нужной длины, форматирует и возвращает их в виде списка + остаток исходной строки"
    position = 0
    final_string = []
    tail = ''
    while position < len(input_string):
        newlinepos = input_string.find('\n', position)
        if newlinepos > line_len or newlinepos == -1:
        # если /n где-то далеко
            #считаем правую границу строки
            boundary = position + line_len
            if boundary >= len(input_string):
            #если остаток исходной строки короче нашей, возвращаем его
                tail = input_string[position:]
                break
            elif input_string[boundary] != ' ':
            #если слово не разрывается, а заканчивается ровно по длине новой строчки
                line_string, _, end = input_string[position:boundary].rpartition(' ')
            else:
            #делаем строку нужной длины
                line_string = input_string[position:boundary]
            #сдвигаемся по исходной на длину извлеченной +пробел
            position = position + len(line_string) + 1
            #форматируем
            line_string = line_fit(line_string, line_len)
        else:
        # если ближе чем заданная длина строки
            line_string = input_string[position:newlinepos]
            position = newlinepos + 1
        final_string.append(line_string)
    #список строк и остаток
    return final_string, tail

line_len = input_len(36)
#открываем оба файла
with open('test.txt','r', encoding='utf--8') as fin:
    with open('result.txt', 'w', encoding='utf--8') as fout:
        tail = ''
        #проходим по строкам исходного
        for line in fin:
            line = tail + line
            string_list, tail = line_extraction(line)
            #полученные строки пишкм в новый
            for lineout in string_list:
                fout.writelines([lineout, '\n'])
        #остаток тоже дописываем
        if tail:
            fout.writelines([tail, '\n'])