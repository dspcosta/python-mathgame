import random

operandList = []
for x in range(0,5):
    operandList = operandList + [x]
    operandList[x] = random.randint(1,9)

operatorDict = {
    1:"+",
    2:"-",
    3:"*",
    4:"**"
}

operatorList = []
for x in range(0,4):
    operatorList = operatorList + [x]
 
    operatorList[x] = [operatorDict[random.randint(1,4)]]

    if operatorList[x - 1][0] == '**':
         operatorList[x] = [operatorDict[random.randint(1,3)]]
    

print(operatorDict)
print(operandList)
print(operatorList)

equation = ' '
for x in range(1,6):
    if x == 5:
        eqpart = str(operandList[random.randint(0,4)])
        equation = equation + eqpart
        break

    eqpart = str(operandList[random.randint(0,4)]) + " " + str(operatorList[random.randint(0,3)][0]) + " "
    equation = equation + eqpart

print(equation)
print(eval(equation))