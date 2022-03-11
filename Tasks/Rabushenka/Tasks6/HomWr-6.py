def list_sum(sum):
    check = 0
    for element in sum:
        if (type(element) == type([])):
            check = check + list_sum(element)
        else:
            check = check + element
    return check
print("Sum of elements:", list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))

number = int(input("Calculating sequences of Fibonacci numbers: "))
def fibonacci(number):
    if (number <= 1):
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))
for i in range(number):
    print(fibonacci(i), end=' ')




