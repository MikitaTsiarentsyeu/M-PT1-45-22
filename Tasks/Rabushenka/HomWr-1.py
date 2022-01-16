import math
Sum = 20000
year = 5
rate = 15
days = 365
exec = days * year
print(f'срок вложения в днях = {exec}')
tran_on = rate / 100
print(f'перевод процентной ставки = {tran_on}')
Final_sum = Sum * (1 + tran_on/days)**exec
print(f'сумма на счету в конце указанного срока = {Final_sum}')