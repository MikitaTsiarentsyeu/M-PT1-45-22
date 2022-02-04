d = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fifteen':'15', 'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19', 'twenty':'20', 'twentyone':'21'}

stroka = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
stroka = stroka.split()

numbers = []
for i in stroka:
    reserve = d.get(i)
    numbers.append(reserve)
    
numbers = list(set(numbers)) # removing duplicates

for i in range(len(numbers)):
    numbers[i] = int(numbers[i]) # cast to int
            
sor_numbers = sorted(numbers)
print(sor_numbers, "- sorted list.")

for i in range(0, len(sor_numbers), 2):
    if i + 1 <= len(sor_numbers) - 1:
        print(f'Product equals: {(sor_numbers[i] * sor_numbers[i+1])}')
    if i + 2 <= len(sor_numbers) - 1:
        print(f'Sum equals: {(sor_numbers[i+1] + sor_numbers[i+2])}')

s = 0
for i in sor_numbers:
  if i % 2 == 1: # checking for odd
    s += i 
print(f'The sum of all odd numbers is {s}.')
