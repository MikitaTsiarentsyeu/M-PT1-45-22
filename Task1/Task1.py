# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет 
# процент (годовой) - 15%
#! ежемесячная капитализация!


# Вычислить сумму на счету в конце указанного срока.

Summ = 20000
Perc = 0.15
Month = 60
Lastsumm = Summ * (1 + (Perc/12))**Month
print(Lastsumm)