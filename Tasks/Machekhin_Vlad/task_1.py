# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет
# процент (годовой) - 15%
# !ежемесячная капитализация!
# Вычислить сумму на счету в конце указанного срока.

P = 20000 # начальная сумма
N = 15/100 # годовая ставка, разделенная на 100
T = 60 # количество месяцев
D = P * ((1+N/12)**T)
print(round(D,2))