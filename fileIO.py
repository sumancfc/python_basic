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


