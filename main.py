import myPythonFunction
import mathGame

try:

    finishProgram = False
    counter = 0

    while finishProgram == False:
    
        if counter > 0:
            optionContinue = int(input('Do you want to do a new search or Update? Yes[1] No[2]:  '))
            if optionContinue == 2:
                print("Thank you, see you soon!")
                break
            elif optionContinue > 2:
                print("Not a valid option, the program will be terminated.")
                break 

        counter = counter + 1

        print('''
        
        ***************************************************
        *                                                 *
        *            WELCOME TO THE SCORE GAME            *
        *                                                 *  
        ***************************************************   

        Please select one of the options below:

        1) Search for a Score from a Specific User Name
        2) Update a Score for a specific User Name
        3) Show All Scores
        4) New Math Game!!!
        5) Quit
        '''
        )
        optionSelect = int(input("Insert option:"))

        if optionSelect == 1:
            searchUser = str(input("Insert the name that you want:"))
            myPythonFunction.getUserPoint(searchUser)
        elif optionSelect == 2:
            optionUpdate = int(input("Is it a New User? Yes[1] No[2]"))
            if optionUpdate == 1:
                newUser = True
                searchUser = str(input("Insert the name that you want to insert Score:"))
                scoreUpdate = int(input("Insert the Score:"))
                myPythonFunction.updateUserPoints(newUser, searchUser, scoreUpdate)
            elif optionUpdate == 2:
                newUser = False
                searchUser = str(input("Insert the name that you want to update the Score:"))
                scoreUpdate = int(input("Insert the New Score:"))
                myPythonFunction.updateUserPoints(newUser, searchUser, scoreUpdate)
        elif optionSelect == 3:
            myPythonFunction.showAllScore()
        elif optionSelect == 4:
            mathGame.mathGame()
        else:
            finishProgram = True
            print('Thank you, see you soon!')

except Exception as e:
    print("An error has occurred! Error: ", e)
