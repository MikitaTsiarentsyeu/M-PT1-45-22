from decimal import Decimal, ROUND_HALF_UP


deposit_amount = Decimal('20000')
deposit_rate = Decimal('15')
deposit_period = Decimal('5')

deposit_result = deposit_amount * ((1 + deposit_rate/(100*12)) ** (deposit_period*12))

print('your balance is', deposit_result.quantize(Decimal('1.00'), ROUND_HALF_UP), 'BYN')
