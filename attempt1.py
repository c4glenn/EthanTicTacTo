End1 = [[1, 1, 0],
        [0, 0, 0],
        [0, 0, 0]]

def checkForEnd(Matrix):
    won = False
    for i in range(0, 3):
        if Matrix[i][0] == Matrix[i][1] and Matrix[i][0] == Matrix[i][2] and Matrix[i][0] != 0: #Check for Row Completion
            print("Player 1 won on row " + str(i+1))
            print(Matrix[0])
            print(Matrix[1])
            print(Matrix[2])
            won = True
        if Matrix[0][i] == Matrix[1][i] and Matrix[0][i] == Matrix[2][i] and Matrix[0][i] != 0: #Check for Column Completion
            print("Player 1 won on Column " + str(i+1))
            print(Matrix[0])
            print(Matrix[1])
            print(Matrix[2])
            won = True

    if Matrix[0][0] == Matrix[1][1] and Matrix[1][1] == Matrix[2][2] and Matrix[0][0] != 0: #Diagonal 1
        print("Player 1 won on Diagonal ")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won =True   
    if Matrix[0][2] == Matrix[1][1] and Matrix[1][1] == Matrix[2][0] and Matrix[0][2] != 0: #Diagonal 1
        print("Player 1 won on Diagonal ")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won = True
    Count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            print(i, j, Matrix[i][j])
            if Matrix[i][j] == 3:
                Count += 1
    if Count >= 3:
        print("Player 2 won")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won = True

    if not won:
        print("No one has won")

def oneMove(Matrix):
    won = False
    for i in range(0, 3):
        if (Matrix[i][0] == Matrix[i][1] and Matrix[i][0] != 0) or (Matrix[i][1] == Matrix[i][2] and Matrix[i][1] != 0): #Check for Row Completion
            print("Player 1 is one away on row " + str(i+1))
            print(Matrix[0])
            print(Matrix[1])
            print(Matrix[2])
            won = True
        if (Matrix[0][i] == Matrix[1][i] and Matrix[0][i] != 0) or (Matrix[1][i] == Matrix[2][1] and Matrix[1][i] != 0): #Check for Column Completion
            print("Player 1 is one away on Column " + str(i+1))
            print(Matrix[0])
            print(Matrix[1])
            print(Matrix[2])
            won = True

    if (Matrix[0][0] == Matrix[1][1] and Matrix[0][0] != 0) or (Matrix[1][1] == Matrix[2][2] and Matrix[1][1] != 0) : #Diagonal 1
        print("Player 1 is one away on Diagonal")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won =True   
    if (Matrix[0][2] == Matrix[1][1] and Matrix[0][2] != 0) or (Matrix[1][1] == Matrix[2][0] and Matrix[2][0] != 0): #Diagonal 1
        print("Player 1 wis one away on Diagonal")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won = True
    Count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            print(i, j, Matrix[i][j])
            if Matrix[i][j] == 3:
                Count += 1
            Else:
                    pass
    if Count = 2:
        print("Player 2 won")
        print(Matrix[0])
        print(Matrix[1])
        print(Matrix[2])
        won = True


checkForEnd(End1)