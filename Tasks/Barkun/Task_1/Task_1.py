#                   Задача

# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет 
# процент (годовой) - 15%
# !ежемесячная капитализация!

# вычислите сумму по счету в конце измерения.

#                    Решение 

# Формула для вкладов с капитализацией: S = D *(1 + n/100/L)**T,

# используемые обозначения:
# S – сумма вклада на дату окончания действия депозита, которую вкладчик получит на руки;
# D – изначально внесенная сумма на депозит с возможностью капитализации;
# n - % ставка (годовая);
# L = 12 - при ежемесячной капитализации 
# T – срок вклада в единицах капитализации

from decimal import Decimal

init_depo = 20000
interest_rate = 15
num_capital_years = 12
years = 5
total_term = num_capital_years * years

final_depo = Decimal(init_depo * (1 + interest_rate/100/num_capital_years)**total_term)

print ("Total deposit amount at the end of the period:  ", final_depo.quantize(Decimal('1.00'))," BYN")