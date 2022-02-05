s=('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen')
l=s.split(" ")
num={("one"):1,("two"):2,("three"):3,("four"):4,"five":5,("six"):6,("seven"):7,("eight"):8,("nine"):9,("ten"):10,("eleven"):11,("twelve"):12,("thirteen"):13,("forteen"):14,("fiveteen"):15,("sixteen"):16,("seventeen"):17,("eighteen"):18,("nineteen"):19,("twelve"):20}
len1=[]
for k in l:
    len1.append(num[k])
len1=sorted(len1)
print(len1)
new_len1=[]
[new_len1.append(item) for item in len1 if item not in new_len1]
print(new_len1)
#x_new=[]
#for x in len1:
#    if x not in x_new:
#            x_new.append(x)
#print(x_new)
sum1=[]
m=new_len1
for m in new_len1:
    if m%2!=0 :
        sum1.append(m)
        
                    
full_summ=sum(sum1)            
print("полная сумма=",full_summ) 

sum_1=[]
proz=[]

for x in range(len(new_len1)):
    if x%2==0 not in new_len1:
        h=new_len1[x]*new_len1[x+1]
        sum_1.append(h)  
        x+=1 
    elif x in range(len(new_len1)-1) :
        c=new_len1[x]+new_len1[x+1]
        proz.append(c)   
print(f'произведение первого и второго, и тд=',sum_1)  
print(f'сумма второго и третьего, и       тд=',proz)
           
    