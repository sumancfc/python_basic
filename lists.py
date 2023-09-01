# myList = ["apple", "banana", "cherry", "apple", "cherry"]
# print(myList)
# print(myList[2])
# print(len(myList))
#
# list = ["abc", 34, True, 40, "male"]
# print(list)
# print(type(list))

# list() constructor
# my_list = list(("apple", "banana", "cherry"))
# print(my_list)
#
# fruits = ["Apple", "Banana", "Cherry"]
# if "Apple" in fruits:
#     print("Apple is Present")

# Change list items
# fruits[1] = "Watermelon"
# print(fruits)

# Change a Range of item values
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# fruits[1:3] = ["watermelon", 'Honeymelon']
# print(fruits)

# Insert Item => insert(index, value)
# fruits.insert(1, "Grape")
# print(fruits)

"""Add List Items
append(), insert(), extend()
"""
# append() method
# alphabets = ["A", "B", "C", "D","E"]
# alphabets.append("F")
# print(alphabets)
#
# alphabets.insert(6, "G")
# print(alphabets)

# extend() method => to append elements from another list
# europe = ["Germany", "Denmark", "France", "Belgium"]
# asia = ["Nepal", "India", "China", "UAE"]
# europe.extend(asia)
# print(europe)

"""Remove List Item
remove(), del(), pop(), clear()
"""
# alphabets = ["A", "B", "C", "D","E"]
# alphabets.remove("A")
# alphabets.pop(0)
# alphabets.pop()
# del alphabets[3]
# del alphabets
# alphabets.clear()
# print(alphabets)

"""Loop Lists
"""
fruits = ["apple", "banana", "cherry"]
#For Loop
# for fruit in fruits:
#     print(fruit)

# loop through the index number
# for fruit in range(len(fruits)):
#     print(fruits[fruit])

# While Loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1
