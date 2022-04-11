# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False


def is_prime(x):
    if x == 1 or x == 0:
        return print(f"{x} - Error")
    if x == 2:
        return print(f"{x} - True")
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            return print(f"{x} - False")
    else:
        return print(f"{x} - True")
    
is_prime(0)    
is_prime(1)
is_prime(2)
is_prime(777)
is_prime(787)