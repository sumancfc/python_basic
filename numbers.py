"""There are three numeric types in python
.i.e int => whole, positive or negative number without decimal of limited length
     float => number, positive or negative containg one or more decimals
     complex => numbers are written with a "j" as the imaginary part
"""

x = 1
y = 1.1
z = 1j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

a = int(y)
b = float(x)
c = complex(y)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random number
# doesnot have random() function to make random number
# but habe built in module called random to make random numbers

import random

print(random.randint(1,10))