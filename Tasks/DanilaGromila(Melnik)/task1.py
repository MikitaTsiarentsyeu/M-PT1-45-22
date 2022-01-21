import decimal
import math
Deposit = 20000#депозит
term = 5 #срок
p = 0.15#процент
month = term*12
bank=decimal.Decimal(p) / decimal.Decimal(12)
S = Deposit * (1 + bank)**month
print(int(S))
