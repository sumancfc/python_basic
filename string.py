# Strings => In python strings are surrounded by either single quote or double quote

print("Hello Python");
print('Hello Python');

x = "Hello World";
print(x);

# Multiline Strings
a = """ 
This is about practicing python basic.
This practice is based on W3School.
"""

print(a)

# We are allowed to use 3 single quote or 3 double quote

# Strings are Arrays
x = "Hello, Python"

print(x[1]) # Get the character at position 1

# Looping through a String
for x in "Apple":
    print(x)

# String Length => len()
i = "Hello ";
print(len(i))

# check string => we use in
x = "This is a python basic";
print("basic" in x); #=> if "basic" is present value is True

# Check if Not
print("Hello" not in x)

# Slicing
b = "Hello World"
print(b[2:8])

# Slice from the start
print(b[:5])

# Slice to the end
print(b[3:])

# Negative Indexing
print(b[-5:-2])

"""Modify Strings"""

#Upper Case
a = "Hello World"
print(a.upper())

# Lowercase
a = "HELLO WORLD"
print(a.lower())

# Remove WhiteSpace
a = " Hello World in Python  "
print(a.strip())

# Replace String
b = a.strip()
print(b.replace("H", "K"))

# Split String
x = "Hello, Python"
print(x.split(","))

# Capatalize
i = "pythoN Programming"
print(i.capitalize())
# Casefold => convert into lowercase
print(i.casefold())

#Center
txt = "Apple"
x = txt.center(10)
print(x)

# Count
txt = "I love apples, apple are my favorite fruit"
x =txt.count('apple')
print(x)

# Encode
txt = "My name is John Doe."
x = txt.encode()
print(x)

# End With Method
x = txt.endswith(".")
print(x)

# Expandtabs() method
txt = "Hello"
x = txt.expandtabs(5)
print(x)

# Find Method
text = "This is a basic python practice"
a = text.find("basic")
print(a)

# Format methos
text = "For only {price:.2f} euro"
print(text.format(price = 49))

name = "My name is {} {}"
print(name.format("John", "Doe"))

# Join Method
names = ("John", "Doe")
name = "-".join(names)
print(name)

# String Concatenation
firstname = "John"
lastname = "Doe"
fullname = firstname + " " + lastname
print(fullname)

# Escape Characters
txt = "I love \"Python\" Programming"
print(txt);