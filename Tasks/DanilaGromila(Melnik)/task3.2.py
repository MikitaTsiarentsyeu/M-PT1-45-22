from collections import Counter
import heapq

string = input ('\nenter your str:\n').lower() 

user_val = int(input ('\nenter quantity:\n'))

if user_val >= len(string): 
    print ('\nstmh wrong')
else:

    simb_str = [',','.','!','?','(',')', ':']       
    for i in simb_str:
        string = string.replace(i,'')

string=sorted(string.split())                   
string = Counter(string)                        
symbols = heapq.nlargest(val, str, key=string.get) 

i = 0                                               
while i <= user_val -1:
    elem_max = string[symbols[i]]
    elem_max_name = symbols[i]
    print ("""\n'""" + elem_max_name + """'""",'встречается', elem_max, 'раза')
    i = i + 1

