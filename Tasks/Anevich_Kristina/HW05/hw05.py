
def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for i in s:
        if i.isupper():
           d["upper_case"]+=1
        elif i.islower():
           d["lower_case"]+=1
        else:
           pass
    
    print ("Original String : ", s)
    print ("Upper case: ", d["upper_case"])
    print ("Lower case: ", d["lower_case"])
    
string_test('Blue Green Red') 


def test_number(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_number(10))   


def get_ranges(l):    
    s = f"{l[0]}"
    res = False        
    for i in range(len(l)-1):             
        if l[i+1]-l[i] == 1:
            res = True            
        else:
            if res:
               s += f"-{l[i]}, {l[i+1]}"
            else:
                s += f", {l[i+1]}"
            res = False
    if res:
        s+= f"-{l[-1]}"

    return s
        
print(get_ranges([3, 5, 6, 7, 10, 14, 21]))