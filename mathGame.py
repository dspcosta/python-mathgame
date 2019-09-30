import random
import myPythonFunction


def mathGame():
    quitGame = False

    while quitGame is False:
        operandList = []
        for x in range(0, 5):
            operandList = operandList + [x]
            operandList[x] = random.randint(1, 9)

        operatorDict = {
            1: "+",
            2: "-",
            3: "*",
            4: "**"
        }

        operatorList = []
        for x in range(0, 4):
            operatorList = operatorList + [x]

            operatorList[x] = [operatorDict[random.randint(1, 4)]]

            if operatorList[x - 1][0] == '**':
                operatorList[x] = [operatorDict[random.randint(1, 3)]]

        equation = ' '
        for x in range(1, 6):
            if x == 5:
                eqpart = str(operandList[random.randint(0, 4)])
                equation = equation + eqpart
                break

            eqpart = str(operandList[random.randint(0, 4)]) + " " + str(
                operatorList[random.randint(0, 3)][0]
                ) + " "

            equation = equation + eqpart

        result = eval(equation)
        display = equation.replace("**", "^")

        newUserQuestion = int(input('Is it a New User? Yes[1] No[2] '))

        if newUserQuestion == 1:

            newScore = 0

            userNameGame = input(
                'Please insert the User Name that will play: '
                )

            print("The equation to be solved is:\n", display)

            valueAnswer = int(input('What is the Result? '))

            if valueAnswer == int(result):
                print('Right answer!! :)')
                newScore = 50

            else:
                print('Wrong answer!! The correct result is: ', result)
                newScore = 0

            myPythonFunction.updateUserPoints(True, userNameGame, newScore)
        else:
            newScore = 0

            userNameGame = input(
                'Please insert the User Name that will play: '
                )

            print("The equation to be solved is:\n", display)

            valueAnswer = int(input('What is the Result? '))

            if valueAnswer == int(result):
                print('Right answer!! :) You got 50 Points!')
                newScore = 50

            else:
                print('Wrong answer!! The correct result is: ', result)
                newScore = 0

            oldScore = int(myPythonFunction.setUserPoint(userNameGame))
            updateScore = oldScore + newScore
            myPythonFunction.updateUserPoints(False, userNameGame, updateScore)

        quitOrNo = int(input(
            'Do you want to continue in the Game? Yes[1] No[2] '
            ))

        if quitOrNo == 1:
            quitGame = False

        else:
            quitGame = True
            print("Thank you, see you later!")