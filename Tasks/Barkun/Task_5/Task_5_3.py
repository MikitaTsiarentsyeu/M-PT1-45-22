# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#  отсортированных по возрастанию, и которая этот список “сворачивает”.

#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#  get_ranges([4,7,10])  -> "4, 7, 10"
#  get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

from ntpath import join
import random

#list_num = ([0, 1, 2, 3, 4, 7, 8, 10])
#list_num = ([4,7,10])
#list_num = ([2, 3, 8, 9])

#Implementation for any random sequence of numbers
list_num = sorted(random.sample(range(25), 19))                     
print ('\nRandom sequence of numbers:\n', list_num, '\n\n')

def get_ranges (list_num):
    list_nam_1 =[]
    count = 0
    quote = (""" " """)
    print ('\nA list of values collapsed into a string: ', quote.replace(' ', ''), end ='')
    #Checking for a sequence of numbers of numbers
    for i in list_num:
        if (list_num[count] + 1) == list_num [count + 1]:
            list_nam_1.append(list_num[count])
            count += 1
           # Checking for the last number of the sequence
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])                                              
                list_nam_1 = (f'{str(list_nam_1[0])}-{(str(list_nam_1[len(list_nam_1) - 1]))}')
                print (list_nam_1, end ='')                                                                    
                quote = (""" " """)
                print (quote.replace(' ', ''), end ='')
                print ('\n\nProgram execution is finished!\n')
                break
        #If not the last number in the sequence
        elif (list_num[count-1] + 1) == list_num [count]:
            list_nam_1.append(i)                                                               
            list_nam_1 = (f'{str(list_nam_1[0])}-{(str(list_nam_1[len(list_nam_1) - 1]))}')    #  
            print (list_nam_1, end=', ')                                                       
            #Zeroing the list to create a new sequence
            list_nam_1 = []
            count +=1
            # Checking for the last number of the sequence
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])
                print (str(list_nam_1[len(list_nam_1) - 1]), end ='')
                quote = (""" " """)
                print (quote.replace(' ', ''), end ='')
                print ('\n\nProgram execution is finished!\n')
                break
        #A new list for a new sequence
        else:
            list_nam_1.append(list_num[count])
            count += 1
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])
                list_nam_1 = ', '.join(map(str, list_nam_1))
                print (list_nam_1, end ='')
                quote = (""" " """)
                print (quote.replace(' ', ''), end ='')
                print ('\n\nProgram execution is finished!\n')
                break
            else:
                print (', '.join(map(str,list_nam_1)), end =', ')
                list_nam_1 = []
                continue
get_ranges(list_num)