from collections import Counter

# Еxercise 1

question = input("enter the string: ")
question_number_1 = int(input("How many items to display?: "))

count_symbols = []

for x in question.split():
    if x in count_symbols:
        count_symbols.append(count_symbols)
    print(f'repeats: {Counter(question).most_common(question_number_1)}')

    # Еxercise 2

question_txt = input("Enter text: ")
question_number_2 = int(input("How many items to display?: "))
count_txt = []
for word in question_txt.split():
    count_word = ""
    for leter in word:
        if leter.isalpha():
            count_word += leter.lower()

    count_txt.append(count_word)

print(Counter(count_txt).most_common(question_number_2))
