'''Депозит:
начальная сумма - 20000 BYN
срок - 5 лет 
процент (годовой) - 15%
!ежемесячная капитализация!
Вычислить сумму на счету в конце указанного срока.
'''

from decimal import Decimal

start_sum = 20000
period = 5
percent = 15

total_amount = Decimal(start_sum * (1 + (percent/12/100))**(period*12)) # 12 months per year

print("Total amount at the end of the deposit term:", total_amount.quantize(Decimal('1.00')), "BYN")