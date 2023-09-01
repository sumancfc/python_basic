print(10 > 8)
print(10 == 9)

a = 100
b = 199

if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

# bool function
print(bool("Hello"))
print(bool(5))

print(bool(False))
print(bool(0))

# function can returm a Boolean
def myFunc():
    return True

print(myFunc())

if myFunc():
    print("Hello Function")
else:
    print("Not a Function")

# isinstance()
x = 400;
print(isinstance(x, int))
