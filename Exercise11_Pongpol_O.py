inputNumber = int(input())
star = "*"
for x in range(inputNumber):
    space = ""
    for y in range(x, inputNumber-1):
        space += " "
    print(space+star)
    star += "**"