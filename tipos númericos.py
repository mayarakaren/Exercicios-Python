dir(int)
dir(float)

a = 5
b = 2.5
a / b
a + b
a * b

type(a)
type(b)
type(a - b)

b.is_integer()
5.0.is_integer()

dir(int)
int.__add__(2, 3)
2 + 3

(-2).__abs__()
abs(-2)

(-3.6).__abs__()
dir(float)
abs(-3.6)

# 1.1 + 2.2
from decimal import Decimal, getcontext
Decimal(1) / Decimal(7)

getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

1.1 + 2.2
getcontext().prec = 10
Decimal(1.1) + Decimal(2.2)

import decimal
dir(decimal)
dir()