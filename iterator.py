my_tuple = ("apple", "banana", "orange")

my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator));
print(next(my_iterator))

fruit = "banana";
single_word = iter(fruit)

print(next(single_word))
print(next(single_word))
print(next(single_word))
print(next(single_word))
print(next(single_word))
print(next(single_word))

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)


class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x <=10:
            a = self.x
            self.x += 1
            return a
        else:
            raise StopIteration


myNumber = MyNumbers()
num_iter = iter(myNumber)

for x in num_iter:
    print(x)
