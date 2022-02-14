# print([i for i in range(1, 101)])

first_div = 3
second_div = 5

start = 1
stop = 201

fizz_token = "Fizz "
buzz_token = "Buzz"

def check_rem(num, div):
    return num%div==0

def mult(token, value):
    return token*value

def main():
    [print((mult(fizz_token, check_rem(i,first_div)) + mult(buzz_token, check_rem(i,second_div)) or i)) for i in range(start, stop)]

main()