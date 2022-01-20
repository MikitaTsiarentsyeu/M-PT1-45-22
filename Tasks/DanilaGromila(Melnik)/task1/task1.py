import decimal
Deposit = 20000
term = 5 
p = 0.15
month = term*12
bank=decimal.Decimal(p) / decimal.Decimal(12)
S = Deposit * (1 + bank)**month
print(S)