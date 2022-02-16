while True:
    line = input("Insert your line length:")
    if line.isdigit():
        line = int(line)
        if line < 35:
            print("Your input is incorrect. The line length must be more than 35 symbols.")
            continue
        else:
            break
    else:
        print("Your input is incorrect. Please submit a digit.")
        continue

with open("txt.txt", "r", encoding = 'utf-8') as f:
    text = f.readlines()

f_text = ""
for x in text:
    words = x.split()
    length = 0
    lines = ""
    for i in words:
        length += len(i) + 1
        if length-1 == line:
            lines += i + "\n"
            f_text += lines
            lines, length = "", 0
            continue
        if length-1 < line:
            lines += i + " "
        if length-1 > line:
            lines = lines[:-1]
            while len(lines) != line:
                spaces = line - len(lines)
                lines = lines.replace(' ', '  ', spaces)
            lines += "\n"
            f_text += lines
            lines, length = i + " ", len(i) + 1,
    f_text += lines + "\n"

with open("result.txt", "w", encoding = 'utf-8') as f:
    f.write(f_text)