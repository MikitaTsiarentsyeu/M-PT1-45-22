d = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fifteen':'15', 'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19', 'twenty':'20', 'twentyone':'21'}

stroka = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
stroka = stroka.split()

numbers = []
for i in stroka:
    reserve = d.get(i)
    numbers.append(reserve)
    
numbers = list(set(numbers)) # убираем дубликаты

for i in range(len(numbers)):
    numbers[i] = int(numbers[i]) # приводим к int
            
sor_numbers = sorted(numbers)
print(sor_numbers, "- отсортированный список.")

print(f'Произведение первого и второго чисел: {sor_numbers[0] * sor_numbers[1]}. Сумма второго и третьего: {sor_numbers[1] + sor_numbers[2]}. Произведение третьего и четвертого: {sor_numbers[2] * sor_numbers[3]}. Сумма четвертого и пятого: {sor_numbers[3] + sor_numbers[4]}. Произведение пятого и шестого: {sor_numbers[4] * sor_numbers[5]} и т.д.')

s = 0
for i in sor_numbers:
  if i % 2 == 1: # проверка на нечетность
    s += i 
print(f'Сумма всех нечетных чисел равна {s}.')
