from math import pow

deposit_amount = 20000
deposit_rate = 15
deposit_period = 5


deposit_result = deposit_amount * pow((1 + deposit_rate/(100*12)), (deposit_period*12))
print(deposit_result)
