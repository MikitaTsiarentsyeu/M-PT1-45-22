from itertools import product

numbers_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
'six': 6, 'seven': 7,'eight': 8, 'nine': 9, 'ten': 10,
'eleven': 11,'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
'twenty-one': 21}
  
string_of_numbers = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

a = string_of_numbers.split()
digit_list = []
for number in a:
     digit = numbers_dict.get(number)
     digit_list.append(digit)

sorted_unique_list = list(set(digit_list))
product_list = []
sum_list = []
odd_numbers =[]

for i in range(len(sorted_unique_list)):
    if len(sorted_unique_list) -1!=i:
        if i==0 or i %2==0:
            product = sorted_unique_list[i]*sorted_unique_list[i+1]
            product_list.append(product)
        else:
            add = sorted_unique_list[i] + sorted_unique_list[i+1]
            product_list.append(add)       
    if sorted_unique_list[i] %2!=0:
        odd_numbers.append(sorted_unique_list[i])

print(digit_list)
print(sorted_unique_list)
print(product_list)
print(odd_numbers)
print(sum(odd_numbers))



















