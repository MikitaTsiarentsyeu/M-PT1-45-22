# 1) a function returns the number of letters in upper and lower case
def check_str (string):   
    upper = 0
    lower = 0
    for word in string.split():
        for i in word:
            if i == i.upper():
                upper +=1
            if i == i.lower():
                lower += 1
    return f'{upper} upper case, {lower} lower case'

print(check_str ('The quick Brown Fox'))

# 2) a function returns "True" for prime numbers
def is_prime (a):
    prime = ''
    for i in range(2, a):
        if a % i == 0:
            prime = 'False'
            break
        else:
            prime = 'True'
    return prime

print(is_prime (787))
print(is_prime (777))

# 3) a function returns minimized list
def get_ranges(list):
    list_new = f'{list[0]}'
    result = False
    for y in range(len(list)-1):
        if list[y + 1] == list [y] + 1:
            result = True
        else:
            if result:
                list_new += f'-{list[y]}, {list[y+1]}'
            else:
                list_new += f', {list[y+1]}'
            result = False
    if result:
        list_new += f'-{list[y+1]}' 
    return list_new

print(get_ranges( [0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges( [4, 7, 10]))
print(get_ranges( [2, 3, 8, 9]))
   
