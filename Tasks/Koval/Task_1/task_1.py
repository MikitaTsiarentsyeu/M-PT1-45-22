# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет 
# процент (годовой) - 15%
#! ежемесячная капитализация!


# Вычислить сумму на счету в конце указанного срока.
import decimal

deposit = 20000
term = 5
percent = 0.15

# counting months
term_in_month = term * 12

# Thx Internet for this magic
# intermediate floating point number calculation
k = decimal.Decimal(percent) / decimal.Decimal(12)

result = deposit * (1 + k)**term_in_month
print (str(round(result,2)) + " BYN")