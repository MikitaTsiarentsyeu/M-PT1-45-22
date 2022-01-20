# Mathematical Solution
# Deposit 20000 BYN
# Term 5 years
# Percent 15%
# Monthly capitalization
# Number of months in a year 12
# ? Deposit amount at the end of the term

import math

D = 20000
P = 0.15 # 15/100
M = 12
T = 5

V = D * ( 1 + P / M )**(T*M)
print (round (V,2), "BYN")






