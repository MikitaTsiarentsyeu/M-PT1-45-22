import math
import decimal
from decimal import Decimal

dep = 20000
perc = 15
term = 5
summ = decimal.Decimal(dep*math.pow((1+perc/(100*12)),term*12))
summ.quantize(Decimal('1.00')) #почему не происходит округления?... (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻
print(summ) 
