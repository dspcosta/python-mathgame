import random, os

fileName = 'userScore.txt'
tmpFile = 'userScore.tmp'

try:

    def getUserPoint(userName):
        f = open(fileName, 'r')
        results = f.readlines()
    
        counter = False
        
        for result in results:
            splitado = result.split(',')
            for innerResult in splitado:
                if counter == True:
                    print('Score: ',innerResult)
                    break

                if innerResult == userName:
                    counter = True
                    continue
            if counter == True:
                break
                
        if counter == False:
            print("Sorry, name not found :( ")

        f.close()

    def setUserPoint(userName):
        f = open(fileName, 'r')
        results = f.readlines()

        counter = False

        newResult = 0
        
        for result in results:
            splitado = result.split(',')
            for innerResult in splitado:
                if counter == True:
                    newResult = int(innerResult)
                    break

                if innerResult == userName:
                    counter = True
                    continue
            if counter == True:
                break

        return newResult    

        if counter == False:
            print("Sorry, name not found :( ")

        f.close()

    def updateUserPoints(newUser, userName, score):
        if newUser == True:
            f = open(fileName, 'a')
            model = "\n{}, {}"
            string = model.format(userName,score)
            f.write(string)
            f.close()
        else:
            inputFile = open(fileName, "r")
            outputFile = open(tmpFile,"a")

            lines = inputFile.readlines()
            
            arrayUsers = []
            for line in lines:
                user = line.split(',')
                arrayUsers.append(user)

            for idx, users in enumerate(arrayUsers):
                if arrayUsers[idx][0] == userName:
                    arrayUsers[idx][1] = str(score) #+ '\n'

                string = "{}, {}\n"
                stringLast = "{}, {}"
                arrayLenght = len(arrayUsers)

            for idx, users in enumerate(arrayUsers):
                userArray = arrayUsers[idx][0]
                scoreArray = arrayUsers[idx][1]
                userArray = userArray.strip()
                scoreArray = scoreArray.strip()
                if (idx + 1) < arrayLenght:
                    outputFile.write(string.format(userArray,scoreArray))
                else:
                    outputFile.write(stringLast.format(userArray,scoreArray))
            
            inputFile.close()
            outputFile.close()
            os.remove(fileName)
            os.rename(tmpFile,fileName)

    def showAllScore():
        f = open(fileName, 'r')
        stringScores ='''{}-{}-{}'''

        lines = f.readlines()
        arrayUsers = []
        for line in lines:
            user = line.split(',')
            arrayUsers.append(user)
        print(len(arrayUsers))
        for idx, users in enumerate(arrayUsers):
            userArray = arrayUsers[idx][0]
            scoreArray = arrayUsers[idx][1]
            userArray = userArray.strip()
            scoreArray = scoreArray.strip()
            print(stringScores.format(idx+1, userArray, scoreArray))

        f.close()

except IOError:
    print("Sorry, file not found! We will create one for you! Try again after")
    f = open(fileName, 'w')
    f.close()
