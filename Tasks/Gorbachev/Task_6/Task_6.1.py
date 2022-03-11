"""1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34"""

import random
 
def list_generator(list_init, len_lst):
    """Return recursively generated list of lists instead of middle element from initial list
    
    Parameters:
        list_g: list
            inititial list of elements
        len_lst : int
            lenght of initial list
    Returns:
        list_g: List
            generated nested list"""
    temp_list = []
    middle = len_lst//2
    for i in range(middle+2): #value 2 is a number of elements in deepest list
        if i != middle: #search for middle of list
            temp_list.append(random.randint(0, 10))
        else:
            if temp_list != []:
                list_init.insert(i, temp_list)
                list_generator(temp_list, len_lst-1)
    return list_init


def recursive_sum(sample):
    """Return sum of all elements from user list of lists
    
    Parameters:
        sample: list
            user list of lists with integers values
    Returns:
        sum_elements: int
            sum of all elements from user list of lists"""
    sum_elements = 0
    for i in sample:
        if not isinstance(i, list): #checking if current element i is list
            sum_elements = sum_elements + i
        else:
            sum_elements = sum_elements + recursive_sum(i)
    return sum_elements


list_gen = [random.randint(0,20) for i in range(random.randint(2, 8))] #generating initial list
sample_list = list_generator(list_gen, len(list_gen))   #recursively generated nested list
#sample_list = [1, 2, [2, 4, [[7, 8], 4, 6]]] #sample from task
print(f'Initial list: {sample_list}, sum of elements - {recursive_sum(sample_list)}')