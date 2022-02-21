def check_str():
    word ="The quick Brow Fox"
    upper=""
    lower="" 
    for i in word:
        if i.isupper() == True:
            upper+=i
            value1=len(upper)
        if i.islower()==True:
            lower+=i
            value2=len(lower)
    print("в нижнем регистре=",value1,"в верхнем регистре=",value2)

check_str()    

def is_prime(x):
    simple=True
    i=2
    n=2
    while i <= x**(1/n):
        if x%i==0:
            simple=False
            break
        i+=1       
    if simple:
        print(f"is_prime({x})->True") 
    else:  
        print(f"is_prime({x})->False")

is_prime(787)
is_prime(777)

def sorted_ranges(numbers):
    numbers = iter(numbers)
    nc = next(numbers)
    nb, ne = nc, nc
    for nc in numbers:
        if nc == ne + 1:
            ne += 1
        else:
            yield nb, ne
            nb, ne = nc, nc
    yield nb, ne
                
def get_rangers(swe):
    ranges = sorted_ranges(swe)
    return print(f"get_rangers{swe}->",','.join('{0}'.format(r[0]) if r[0] == r[1] else '{0}-{1}'.format(r[0], r[1]) for r in ranges))
        
get_rangers([2, 3, 8, 9])


