class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    def printname(self):
        print(self.firstName, self.lastName)


class Student(Person):
    def __init__(self, fName, lName, year):
        super().__init__(fName, lName)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)


x = Student("John", "Doe", 2024)
x.welcome()

