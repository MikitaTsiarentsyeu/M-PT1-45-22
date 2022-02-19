# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#  отсортированных по возрастанию, и которая этот список “сворачивает”.

#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#  get_ranges([4,7,10])  -> "4, 7, 10"
#  get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

from ntpath import join
import random

list_num_1 = ([0, 1, 2, 3, 4, 7, 8, 10])
list_num_2 = ([4,7,10])
list_num_3 = ([2, 3, 8, 9])

#Implementation for any random sequence of numbers
list_num = sorted(random.sample(range(30), 20))                     
print ('\nRandom sequence of numbers:\n', list_num, '\n\n')

def get_ranges (list_num):
    count = 0
    quote = (""" " """)
    list_nam_1 =[]
    print (f"""\nA list of values collapsed into a string:\nget_ranges({list_num}) --> {quote.replace(' ', '')}""", end ='')
    
    #Checking for a sequence of numbers of numbers
    for i in list_num:
        if (list_num[count] + 1) == list_num [count + 1]:
            list_nam_1.append(list_num[count])
            count += 1
           
           # Checking for the last number of the sequence
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])                                              
                return_print = f"""{str(list_nam_1[0])}-{(str(list_nam_1[len(list_nam_1) - 1]))}" """
                return return_print 
            
        #If not the last number in the sequence
        elif (list_num[count-1] + 1) == list_num [count]:
            list_nam_1.append(i)                                                               
            list_nam_1 = f'{str(list_nam_1[0])}-{(str(list_nam_1[len(list_nam_1) - 1]))}'   
            print (list_nam_1, end=', ')                                                       
            
            #Zeroing the list to create a new sequence
            list_nam_1 = []
            count +=1
           
            # Checking for the last number of the sequence
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])
                return_print = f"""{str(list_nam_1[len(list_nam_1) - 1])}" """
                return return_print
                
        #A new list for a new sequence
        else:
            list_nam_1.append(list_num[count])
            count += 1
            if len(list_num) == count + 1:
                list_nam_1.append(list_num[count])
                list_nam_1 = ', '.join(map(str, list_nam_1))
                return_print = f"""{list_nam_1}" """
                return return_print
                
            else:
                print (f"{', '.join(map(str,list_nam_1))}", end =', ')
                list_nam_1 = []
                continue


print (get_ranges(list_num))

print (get_ranges(list_num_1))

print (get_ranges(list_num_2))

print (get_ranges(list_num_3))

print ('\n\nProgram execution is finished!\n')