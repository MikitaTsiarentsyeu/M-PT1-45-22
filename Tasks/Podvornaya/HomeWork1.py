import decimal

deposit = decimal.Decimal('20000')
term = 0
profit = decimal.Decimal('0.15')

while term <60:
    deposit = deposit + (deposit * (profit / decimal.Decimal('12')))
    deposit = round(deposit, 2)
    term +=1

print('Ваш депозит составляет: ', deposit)