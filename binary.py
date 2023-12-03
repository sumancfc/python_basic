n = 8
reminders = []

while n>0:
       # reminder = n%2
       # reminders.append(reminder)
       # # print(reminder)
       # # print(n//2)
       # n//=2
       n, reminder = divmod(n,2)
       reminders.append(reminder)

reminders.reverse()
print(reminders)

print(bin(8)) # bin() for binary