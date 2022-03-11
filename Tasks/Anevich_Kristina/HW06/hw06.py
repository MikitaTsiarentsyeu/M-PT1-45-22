def sum_nestedlist(l):
    # указать, что глобальная переменная
    # упоминается здесь в этой функции
    total = 0 
    for j in range(len(l)):
        if type(l[j]) == list :
            # вызвать ту же функцию, если
            # элемент представляет собой список
            total += sum_nestedlist(l[j])
        else:
            # если это один элемент
            # а не список, добавляем его в итог
            total += l[j]     
    return total            
print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))



def Fibonacci(number):     
    if number == 1:
        return [0, 1]    
    feb_row = Fibonacci(number-1)
    feb_row.append(feb_row[-1]+feb_row[-2])
    return feb_row

print(Fibonacci(5)) 
 
