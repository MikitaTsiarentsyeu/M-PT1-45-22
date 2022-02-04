from collections import Counter
import heapq

string = input ('\nenter your str:\n')

val = int(input ('enter quantity:\n'))

if val >= len(string):
    print ('\nsmth wrong')
else:
    string = Counter(string) 
    symbols = heapq.nlargest(val, str, key=string.get)    
    i = 0                                                               
    while i <= val -1:
        max_elem = string[symbols[i]]
        max_elem_name = symbols[i]
        print ("""\n'""" + max_elem_name + """'""",'встречается', max_elem, 'раза')
        i = i + 1
