flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]

prompt = "Choose your flavor: "

# while True:
#        choice = input(prompt)
#        if choice in flavors:
#               break
#        print(f'Sorry, {choice} is not a valid option.')

# print(f'You choose {choice}')

#### With walrus operator :=

while (choice := input(prompt)) not in flavors:
       print(f'Sorry, {choice} is not a valid option.')
print(f'You choose {choice}.')