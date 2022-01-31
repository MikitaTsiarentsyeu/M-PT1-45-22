from datetime import datetime

# used a function to make program run over again when user types a wrong answer


def what_time():
    x = input("Please choose a time option. Type 'Now' for showing recent time or 'Custom' for showing your time.")
    if x == "Now":
        return datetime.now().time()
    elif x == "Custom":
        return input("Please type your time in HH:MM format:")
    else:
        print(f"There is no option like {x}. Please try again.")
        what_time()


time = what_time()

time = str(time)
time = time.replace(" ", "").split(":")

print(f"{time[0]}:{time[1]}")

hours = int(time[0])
minutes = int(time[1])

# russian dictionaries

hour_dict = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
             10: "десять", 11: "одиннадцать", 12: "двенадцать", 0: "", 13: "тринадцать", 14: "четырнадцать",
             15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", "1": "одна",
             "2": "две"}
genitive = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого", 7: "седьмого",
         8: "восьмого", 9: "девятого", 10: "десятого", 11: "одиннадцатого", 12: "двенадцатого"}
dozens = {2: "двадцать", 3: "тридцать", 4: "сорок"}
genitive_min = {1: "одной", 2: "двух", 3: "трёх", 4: "четырех", 5: "пяти", 6: "шести", 7: "семи", 8: "восьми",
         9: "девяти", 10: "десяти", 11: "одиннадцати", 12: "двенадцати", 13: "тринадцати", 14: "четырнадцати",
         15: "пятнадцати"}


# recalculating 24H into 12H to optimize key amount
if hours > 12:
    hours = hours - 12

# choosing a pattern
if minutes == 0:
    rus_hour = "час" if hours == 1 else "часа" if 1 < hours < 5 else "часов"
    print(f"ровно {hour_dict[hours]} {rus_hour}")
elif minutes < 30 or 30 < minutes < 45:
    if minutes < 20:
        rus_min = "минута" if minutes == 1 else "минуты" if 1 < minutes < 5 else "минут"
        minutes = "1" if minutes == 1 else "2" if minutes == 2 else minutes
        print(f"{hour_dict[minutes]} {rus_min} {genitive[hours+1]}")
    else:
        minutes1 = minutes // 10
        minutes2 = minutes % 10
        rus_min = "минута" if minutes2 == 1 else "минуты" if 1 < minutes2 < 5 else "минут"
        minutes2 = "1" if minutes2 == 1 else "2" if minutes2 == 2 else minutes2
        print(f"{dozens[minutes1]} {hour_dict[minutes2]} {rus_min} {genitive[hours+1]}")
elif minutes == 30:
    print(f"половина {genitive[hours+1]}")
else:
    minutes = 60 - minutes
    rus_min = "минуты" if minutes == 1 else "минут"
    print(f"без {genitive_min[minutes]} {rus_min} {hour_dict[hours+1]}")