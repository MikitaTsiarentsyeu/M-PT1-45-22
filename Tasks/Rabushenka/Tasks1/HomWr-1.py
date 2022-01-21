import math
Sum = 20000
year = 5
rate = 15
days = 365
exec = days * year
print(f'investment period in days = {exec}')
tran_on = rate / 100
print(f'interest rate transfer = {tran_on}')
Final_sum = Sum * (1 + tran_on/days)**exec
Final_sum_M = round(Final_sum,2)
print(f'account balance at the end of the term = {Final_sum_M}')
