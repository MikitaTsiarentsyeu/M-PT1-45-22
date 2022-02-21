def is_prime(x):
    for i in range(2, x):
        if not (x % i) :
            return False
    return True

for i in range(1, 100):
    print('{} {} число {}'.format(i, 'простое' if  is_prime(i) else 'составное', (i == 1) * '\r это ж единица' ))