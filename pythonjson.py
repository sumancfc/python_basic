# JSON is a syntax for storing and exchanging data
# JSON is text, written with Javascript ObjectNotation.

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

a = {
    "name": "John Doe",
    "age" : 30
}

b = json.dumps(a)

print(b)


person = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(person, indent=5, sort_keys=True))