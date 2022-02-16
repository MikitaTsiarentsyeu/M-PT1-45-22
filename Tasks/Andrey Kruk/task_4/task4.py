while True:
    n = input("Enter the length of your line:")
    if n.isdigit():
        n = int(n)
        if n < 35:
            print("Your line must include at least 35 symbols.")
            continue
        else:
            break
    else:
        print("Please, enter a digit.")
        continue

with open('task4.txt', 'r', encoding="utf-8") as f:
    text = f.read().split()
    text_result = ''
    string = ''
    length = 0
    i = 0
    while True:
        length += len(text[i]) + 1
        string += text[i] + ' '
        i += 1

        if (length - 1) == n:
            text_result += string + '\n'
            string = ''
            length = 0

        if (length - 1) > n:
            s = string[:n].rfind(' ')
            spaces = len(string[:n]) - len(string[:s])
            list = string[:s].split()
            x = 0
            while spaces != 0:
                list[x] += ' '
                spaces -= 1
                x += 1
                if x == (len(list) - 1):
                    x = 0
            result = ' '.join(list)
            text_result += result + '\n'
            string = ''
            length = 0
            i -= 1
        if i == (len(text)):
            text_result += string
            break
with open('result_text.txt', 'w', encoding="utf-8") as f:
    f.write(text_result)
