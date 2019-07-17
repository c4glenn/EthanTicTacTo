import numpy as np

blankboard = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]])

board1 = np.array([
    [1, 1, 0],
    [0, 0, 0],
    [0, 0, 0]])

board2 = np.array([
    [1, 2, 0],
    [0, 1, 3],
    [3, 2, 1]])

board3 = np.array([
    [3, 1, 0],
    [3, 0, 1],
    [2, 2, 3]])

board4 = np.array([
    [3, 1, 0],
    [3, 0, 1],
    [3, 2, 2]])

nums = []
boards = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

def checkForEnd(board):
    won = False
    for i in range(0, 3):
        if board.item(i, 0) == board.item(i, 1) and board.item(i, 0) == board.item(i, 2) and board.item(i, 0) != 0: #Check for Row Completion
            print(board)
            print("Player 1 won on row " + str(i+1))

            won = True
        if board.item(0, i) == board.item(1, i) and board.item(0, i) == board.item(2, i) and board.item(0, i) != 0: #Check for Column Completion
            print(board)
            print("Player 1 won on Column " + str(i+1))

            won = True

    if board.item(0, 0) == board.item(1, 1) and board.item(1, 1) == board.item(2, 2) and board.item(0, 0) != 0: #Diagonal 1
        print(board)
        print("Player 1 won on Diagonal ")
        won =True   
    if board.item(0,2) == board.item(1, 1) and board.item(1, 1) == board.item(2, 0) and board.item(0, 2) != 0: #Diagonal 1 
        print(board)
        print("Player 1 won on Diagonal ")
        won = True

    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board.item(i, j) == 3:
                count += 1
    if count >= 3:
        print(board)
        print("Player 2 won")
        won = True

    if not won:
        print(board)
        print("No one has won")

def createNums():
    for i in range(1, 262144):
        num = np.base_repr(i, 4, 9 - len(np.base_repr(i, 4)))
        print("num: " + num)
        a = np.reshape(np.array([int(x) for x in num]), (3, 3))
        print(a)
        print("---------")

def createBoards():
    for i in nums:
        newBoard = np.reshape(np.fromstring(i, dtype=int, sep=''), (3, 3))
        print(nums[1])
        print(np.fromstring(i, int))
        print("newBoard: " + newBoard)
        flip1 = np.rot90(newBoard)
        print("flip1: " + flip1)
        flip2 = np.rot90(newBoard, 2)
        print("flip2: " + flip2)
        flip3 = np.rot90(newBoard, 3)
        print("flip3: " + flip3)
        for i in boards:
            if i == flip1:
                pass
            elif i == flip2:
                pass 
            elif i == flip3:
                pass
            else:
                boards.append(newBoard)

createNums()
print("-----------------------------")
#createBoards()