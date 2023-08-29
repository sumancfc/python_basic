"""
Casting => specify a type on to a variables
Casting in python is done using constructor functions
"""

# int() =>  constructs an integer number from an integer literal,
# a float literal (by removing all decimals), or
# a string literal (providing the string represents a whole number)
x = int(1)
y = int(2.1)
z = int("3")

# float() - constructs a float number from an integer literal, a
# float literal or a string literal (providing the string represents a float or an integer)
x = float(1)
y = float(2.1)
z = float("3")

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
x = str("A1")
y = str(2)
z = str(2.1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))