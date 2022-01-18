import decimal


dep = 20000
year = 5
godProc = 15
monthNum = 12
procMult = 0.01
summ = 0
iter = 0
proc = decimal.Decimal(godProc/monthNum)*decimal.Decimal(procMult) #Задаю переменные(все что выше)
summ = dep #потому что начальная сумма это наш дипозит(и с таким равенством легче написать цикл)
while iter != year*monthNum: # пока у нас количество месяцев не будет равно 60(т.е 5 годам) то мы будем выполнять цикл
    summ = summ+summ*proc
    iter = iter + 1
print('Сумма на балансе через 5 лет в белорусских рублях: ',summ,'; Количество месяцев пока деньги лежат в банке: ',iter)





    


 
   






