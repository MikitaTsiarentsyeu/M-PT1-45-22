
while True:
    user = input("Введите длину строки больше 35:\n")
    if user.isdigit():
        user = int(user)
        if user < 35:
            print("Длина строки должна быть больше 35 символов! Повторите попытку.\n")
            continue
        else:
            break
    else:
        print("Пожалуйста, введите цифру!\n")
        continue

with open("text.txt", "r", encoding = 'utf-8') as f:
    text = f.readlines()
    print(text)
    
new_text = ""

for x in text:
    words = x.split()
    width = 0
    line = ""
    for i in words:
        width += len(i) + 1
        if width-1 == user:
            line += i + "\n"
            new_text += line
            line, width = "", 0
            continue
        if width-1 < user:
            line += i + " "
        if width-1 > user:
            line = line[:-1]
            while len(line) != user:
                place = user - len(line)
                line = line.replace(' ', '  ', place)
            line += "\n"
            new_text += line
            line, width = i + " ", len(i) + 1,
    new_text += line + "\n"

with open("new_text.txt", "w", encoding = 'utf-8') as f:
    f.write(new_text)     