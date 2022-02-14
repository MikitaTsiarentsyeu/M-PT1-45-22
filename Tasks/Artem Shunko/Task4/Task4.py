#1. Прочитать содержимое файла text.txt
#2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
#3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую,
#а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
#4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
#(модуль textwrap использовать нельзя)

def input_len(len1=15):
     while True:
         value = input('Введите количество символов в стоке, не больше 35:')
         if value.isdigit():
             value = int(value)
             if value >= len1:
                 return value

def line2(line_str, line_len):
     
     line_str = line_str.strip()
     
     space_number = line_str.count(' ')
     
     add_len = line_len - len(line_str)
     
     if not space_number or add_len == 0:
         return line_str
     
     a, b = divmod(add_len, space_number)
    
     line_str = line_str.replace(' ', ' '*(a+1))
    
     line_str = line_str.replace(' '*(a+1), ' '*(a+2), b)
     return line_str

def line_extraction(input_str):
     position = 0
     final_str = []
     tail = ''
     while position < len(input_str):
         newlinepos = input_str.find('\n', position)
         if newlinepos > line_len or newlinepos == -1:
         
             boundary = position + line_len
             if boundary >= len(input_str):
             
                 tail = input_str[position:]
                 break

             elif input_str[boundary] != ' ':
             
                 line_str, _, end = input_str[position:boundary].rpartition(' ')
             else:
             
                 line_str = input_str[position:boundary]
             position = position + len(line_str) + 1
             line_str = line2(line_str, line_len)
         else:
         
             line_str = input_str[position:newlinepos]
             position = newlinepos + 1
         final_str.append(line_str)
    
     return final_str, tail

line_len = input_len(36)

with open('test.txt','r', encoding='utf--8') as fin:
     with open('result.txt', 'w', encoding='utf--8') as fout:
         tail = ''
        
         for line in fin:
             line = tail + line
             str_list, tail = line_extraction(line)
             
             for lineout in str_list:
                 fout.writelines([lineout, '\n'])
      
         if tail:
             fout.writelines([tail, '\n'])
