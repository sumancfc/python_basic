fileName = "inputFile.txt"
file = open(fileName, "r")
op1 = "passFile.txt"
op2 = "failFile.txt"

passFile = open(op1, "w")
failFile = open(op2, "w")

for line in file:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)


passFile.close()
failFile.close()

# f = open("passFile.txt", 'r')
# print(f.read(10))
# print(f.readline())
# print(f.readline())
# for x in f:
#     print(x)
#
# f.close()

# f = open("textFile.txt", "a")
# f.write("This is a new line.")
# f.close()
#
# f = open("textFile.txt", "r")
# print(f.read())

# f = open("textFile.txt", "w")
# f.write("This is a new content")
# f.close()
#
# f = open("textFile.txt", "r")
# print(f.read())

import os

if os.path.exists("textFile.txt"):
    os.remove("textFile.txt")
else:
    print("The file does not exist")

# to remove folder => os.rmdir("folder_name)
