def check_str(some_string):
    count_upper = 0
    count_lower = 0
    for i in some_string:
        if i.isalpha() and i == i.upper():
            count_upper += 1
        elif i.isalpha() and i == i.lower():
            count_lower += 1
    return f'{count_upper} upper case, {count_lower} lower case'


print(check_str('The quick Brow Fox'))


def is_prime(n):
    i = 2
    j = 0
    while i**2 <= n:
        if n % i == 0:
            j = 1
            break
        i += 1
    if j == 1:
        return False
    return True


print(is_prime(777))


def get_ranges(some_list):
    ranges_list = []
    i = 0
    j = 0
    some_list.sort()
    some_list.append('')
    while True:
        if j == (len(some_list)-1):
            break
        elif some_list[j+1] != some_list[j] + 1:
            ranges_list.append(some_list[j])
            i = j + 1
            j += 1
        elif some_list[j+1] == some_list[j] + 1:
            j += 1
            if some_list[j+1] != some_list[j] + 1:
                ranges_list.append(f'{some_list[i]}-{some_list[j]}')
                i = j + 1
                j += 1
    return ranges_list


print(get_ranges([2,8,11]))