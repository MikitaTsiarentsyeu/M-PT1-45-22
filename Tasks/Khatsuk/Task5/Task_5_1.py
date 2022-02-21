def check_str(s):
    low_counter = 0
    upp_counter = 0
    for char in s:
        if char.islower():
            low_counter += 1
        elif char.isupper():
            upp_counter += 1
    return '{} upper case, {} lower case'.format(upp_counter, low_counter)

print(check_str('Upper Lower      34 %%% УККАП    ffgfggf '))
