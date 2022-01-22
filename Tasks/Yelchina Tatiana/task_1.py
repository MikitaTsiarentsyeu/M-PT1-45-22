'''Депозит:
начальная сумма - 20000 BYN
срок - 5 лет 
процент (годовой) - 15%
!ежемесячная капитализация!
Вычислить сумму на счету в конце указанного срока'''

amount = 20000 #amount on the start
percent = 15 # year insert rate
month = 12 # months in the year
period = 60 #period of deposit

summa = amount * (1 + percent/(100 * month)) ** period
print (f'The deposit amount at the end of the term = {str(round(summa,2))} BYN')
