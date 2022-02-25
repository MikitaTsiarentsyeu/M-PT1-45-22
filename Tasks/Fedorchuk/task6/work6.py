def Calsum(a):
    sum = 0 
    for t in a:        
        if not isinstance(t, list): 
            sum = sum + t 
        else:            
            sum = sum + Calsum(t)
    return sum
print("сумма элементов=",Calsum([1, 2, [2, 4, [[9, 8], 4, 6]]]))

def fibonacci1(n):
        if(n <= 1):
            return n
        else:
            return fibonacci1(n - 1) + fibonacci1(n - 2)
 
n=int(input("Введите число членов последовательности:"))
#for i in range(n): 
 #    print(f"fib{n}->",(fibonacci1(i))) 
print(f"fib {n}->",[fibonacci1(i) for i in range(n)] ) 
 
