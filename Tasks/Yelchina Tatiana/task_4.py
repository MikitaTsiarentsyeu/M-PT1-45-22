while True:
    symbol = input('Input the number ')

    if not symbol.isdigit(): 
        print ('Invalid input, the number must be a digit')
        continue
    
    symbol = int(symbol)

    if symbol < 35:
        print ('Incorrect input, the number must be > 35')
        continue
    
    break

with open ("text.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        length = 0
        text_new = "" # a new formated text
        string = ""  # a string limited to a given number of symbols
        for word in line.split():    # choose words and length of string
            length += len(word) + 1
            if length - 1 > symbol: 
                string = string[:-1]   # delete spaces
                while len(string) != symbol:
                    space = symbol - len(string)
                    string = string.replace(' ', '  ', space)
                string += '\n'
                text_new += string 
                length = len(word) + 1   
                string = ""              
            string += word + " " 
        text_new += string 
        print(text_new)

with open ("text_new.txt", 'w', encoding = 'utf-8') as f:
    f.write(text_new)
print ('The new formatted file is written to "text_new.txt"')
