
max_count_alpha=int(input("Максимальное количество символов в строке не менее 35=")) 
if max_count_alpha<=35:
    print("Ошибка количества символов в строке,введите еще раз")
    max_count_alpha=int(input("Максимальное количество символов в строке="))
print(max_count_alpha)

with open(r"test.txt", "r", encoding = 'utf-8') as f:
    text = f.read()
f_text = ""
words = text.split()
alpha_lenght = 0
stroki = ""
for i in words:
    alpha_lenght += len(i)+1 
    if alpha_lenght-1 == max_count_alpha:
        stroki += i+ "\n"
        f_text += stroki
        stroki, alpha_lenght = "", 0
        continue
    if alpha_lenght-1 < max_count_alpha:
        stroki += i + " "
    if alpha_lenght-1 > max_count_alpha:
        stroki = stroki[:-1]
        while len(stroki) != max_count_alpha:
                stroki = stroki.replace(' ', '  ',max_count_alpha-len(stroki))
                if len(stroki) == max_count_alpha:
                   break
        stroki += "\n"
        f_text += stroki
        stroki, alpha_lenght = i+ " " , len(i)+1       
f_text += stroki
print(f_text)
with open("text_new.txt", "w", encoding = 'utf-8') as f:
    f.write(f_text) 
    
