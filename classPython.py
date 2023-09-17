average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Suman", "grades": [100,100,40,50,100]},
    {"name": "Shusma", "grades": {50, 90, 40, 50}}
]

for student in students:
    print(average(student["grades"]))