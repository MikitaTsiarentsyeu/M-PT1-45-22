text = input("Input your text:").lower()
repeats = input("Input how many words to display:")

while True:
    if repeats.isdigit():
        repeats = int(repeats)
        break
    else:
        repeats = input("Your input is incorrect. Please print a digit:")
        continue

text = text.split()
text_dict = {}

for i in text:
    count = 0
    for j in text:
        if i == j:
            count +=1
    text_dict.update({i: count})

sorted_text = sorted(text_dict.items())



def sort_key(x):
    return x[1]

sorted_text = sorted(sorted_text, key = sort_key, reverse=True)

count = 0
for i in range(repeats):
    while count < len(sorted_text):
        print(f"word {sorted_text[count][0]} repeats {sorted_text[count][1]} times")
        count+=1
    else:
        print("End of the list, can't print more")
        break