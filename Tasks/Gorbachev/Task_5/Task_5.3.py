"""3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
отсортированных по возрастанию, и которая этот список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"""

import random

def random_list():
    """Generate random ascending sorted list of integer values.
    
    Returns:
        list_random: list
            randomly generated ascending sorted list of integer values"""
    len_list = random.randint(2, 20) #random len between 2 and 15
    list_random = list(set([random.randint(0,20) for i in range(len_list)]))  #random generated list of integer values between 0 and 20 with random lenght between 2 and 15
    list_random.sort()
    return list_random

def get_ranges(list_int):
    """Function returns string with folded sequences of increasing numbers
    
     Parameters:
        list_int: list
            ascending sorted list of integer values
    Returns:
        fold_ranges_str: str
            string with folded sequences from initial string"""
    fold_ranges = []
    fold_ranges_str = ""
    initial, end = -1, -2                                                          
    for item in list_int:  # creating list of sequences from list of numbers
        if item != end+1:                        
            if initial != -1:
                fold_ranges.append([initial, end])
            initial = item
        end = item
    fold_ranges.append([initial, end])
    for i in range(len(fold_ranges)):  # converting list of sequences to a string of sequences
        if fold_ranges[i][0] == fold_ranges[i][1]:
            fold_ranges_str += f'{fold_ranges[i][0]}, '
        else:
            fold_ranges_str += f'{fold_ranges[i][0]}-{fold_ranges[i][1]}, '
    fold_ranges_str = fold_ranges_str[:-2]
    return fold_ranges_str


range_list = random_list() #generating of random sorted list
print(f'Initial list: {range_list}\n{get_ranges(range_list)}')