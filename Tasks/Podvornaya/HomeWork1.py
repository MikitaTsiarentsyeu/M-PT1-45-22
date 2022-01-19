#first solution using while
import decimal

deposit = decimal.Decimal('20000')
term = 0
profit = decimal.Decimal('0.15')

while term <60:
    deposit = deposit + (deposit * (profit / decimal.Decimal('12')))
    deposit = round(deposit, 2)
    term +=1

print('Your deposit is worth: ', deposit, 'BYN')

#second solution using complex persent formula

profit = 1 + 15 / (12*100) ** 60 #mounthly capitalization interest
profit = decimal.Decimal(profit)
deposit = deposit * profit
deposit = round(deposit, 2)
print('Your deposit is worth: ', deposit, 'BYN')