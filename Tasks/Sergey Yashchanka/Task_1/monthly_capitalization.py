# Задание:

# Депозит:
# начальная сумма - 20000 BYN
# срок - 5 лет
# процент (годовой) - 15%
# !ежемесячная капитализация!

# Вычислить сумму на счету в конце указанного срока.

# ------------------------------------------------------------------------------------------------------------------ #

# Решение N_1: EASY LEVEL !!!

# formula monthly capitalization
# S = D * ((1 + (n / 100) / M) ** (T * M - 1))
#
# S - account balance at the end of the term!
# D - initial deposit amount!
# n - annual interest!
# M - number of months in the year!


initial_sum = 20000
period = 5
annual_interest = 15
MONTHS_IN_YEARS = 12

# find the total amount on the account using the formula
total_sum = initial_sum * pow((1 + (annual_interest / 100) / MONTHS_IN_YEARS), (period * MONTHS_IN_YEARS - 1))
print(f"Сумма на счету в конце указанного срока составит: {str(total_sum)[:5]}р {str(total_sum)[6:8]}k")


# ------------------------------------------------------------------------------------------------------------------ #  

# Решение N_2: EASY LEVEL ++ !!!

def monthly_capitalization(init_sum: int = 20000, an_interest: int = 15, per: int = 5, mon_years: int = 12) -> str:
    """return the amount on the account after the monthly capitalization for the specified period"""

    # add percentage to the original amount
    total_summa = init_sum
    for _ in range(per * mon_years - 1):
        total_summa += total_summa / 100 * (an_interest / mon_years)
    return f"Сумма на счету в конце указанного срока составит: {str(total_summa)[:5]}р {str(total_summa)[6:8]}k"


print(monthly_capitalization())
