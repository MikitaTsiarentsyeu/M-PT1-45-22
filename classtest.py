single_variable = {
    "array_words": ["four", "eight", "ten", "one", "one", "eight", "five", "nine", "eleven", "twelve"], 
    "array_numbers": [],
    "transform_words_to_numbers": {
        "zerro": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "sevetneen":17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
    },
    "odd_sum": 0
}

for word in single_variable["array_words"]:
    single_variable["array_numbers"].append(single_variable["transform_words_to_numbers"][word]) # перевел слова в цифры

single_variable["array_numbers_without_duplicates"] = list(dict.fromkeys( single_variable["array_numbers"])) # удалил дубликаты

single_variable["array_numbers_without_duplicates_sorted"] = sorted(single_variable["array_numbers_without_duplicates"]) # отсортировал

for i in range(len(single_variable["array_numbers_without_duplicates_sorted"]) - 1):
    print(single_variable["array_numbers_without_duplicates_sorted"][i] + single_variable["array_numbers_without_duplicates_sorted"][i+1]) # сумма пар элементов

for i in single_variable["array_numbers_without_duplicates_sorted"]:
    if i%2 == 1:
        single_variable["odd_sum"] += i # сумма нечетных

print(single_variable)

