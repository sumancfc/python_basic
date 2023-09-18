import datetime

date = datetime.datetime.now()

print(date.year)
print(date.strftime("%A"))


try:
    f = open("inputFile.txt")
    try:
        f.write("Lorem ipsum")
    except:
        print("Something went wrong while writing the file")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file")


# x = -1
#
# if x < 0:
#     raise Exception("Sorry, No numbers below zero")


# Python String Formatting
price = 49.99
text = "The price is {} euros"

print(text.format(price))