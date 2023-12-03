names = ['Suman', 'Shusma', 'Shrestha', 'Thapa']
ages = [28,27,29,26]
subjects = ['Science', 'Math', 'Social', 'Nepali']

# for position in range(len(ages)):
#        name = names[position]
#        age = ages[position]
#        print(name, age)

# for position, name in enumerate(names):
#        age = ages[position]
#        print(name,age)


# for name, age, subject in zip(names, ages,subjects):
#        print("This is from zip",name, age, subject)

for data in zip(names, ages, subjects):
       name, age, subject = data
       print(name, age, subject)