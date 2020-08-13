 # player is either 1 for X's or 2 for O's

board = [0,0,0,0,0,0,0,0,0] # these can be strings not just numbers i.e. [" ", "X", " ", " ", "O",....]

fancyboard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def printFancyBoard():
    print("   " + fancyboard[0], end="")
    print("   |  " + fancyboard[1], end="")
    print("   |  " + fancyboard[2], end="")
    print()
    print("-------|------|------")
    print("   " + fancyboard[3], end="")
    print("   |  " + fancyboard[4], end="")
    print("   |  " + fancyboard[5], end="")
    print()
    print("-------|------|------")
    print("   " + fancyboard[6], end="")
    print("   |  " + fancyboard[7], end="")
    print("   |  " + fancyboard[8], end="")
    print()

printFancyBoard()
fancyboard[3] = "X"
printFancyBoard()

def printBoard():
    for pos in range(0,9):
        if pos != 0 and pos % 3 == 0:
            print()
            print("-|-|-") 
        if pos % 3 == 1:
            print("|", end="")
            if board[pos] == 0:
                print(pos, end="")
            else:
                if board[pos] == 1:
                    print("X", end="")
                else:
                    print("O", end="")
            print("|", end="")
        else:
            if board[pos] == 0:
                print(pos, end="")
            else:
                if board[pos] == 1:
                    print("X", end="")
                else:
                    print("O", end="")
    print()

#Check to see if there is a three in a row and return's players value
# returns 0 if no winner is found
def checkBoard(player):
    if board[4] == player:
        if board[3] == player:
            if board[5] == player:
                return player
        if board[1] == player:
            if board[7] == player:
                return player
        if board[2] == player:
            if board[6] == player:
                return player
        if board[0] == player:
            if board[8] == player:
                return player
        
    if board[2] == player:
        if board[1] == player:
            if board[0] == player:
                return player
        if board[5] == player:
            if board[8] == player:
                return player
        
    if board[6] == player:
        if board[3] == player:
            if board[0] == player:
                return player
        if board[7] == player:
            if board[8] == 0:
                return player
    
    return 0

while True:
    if 0 in board:
        printBoard()
        player1 = int(input("Please input the space number you would like to player your X "))
        board[player1] = 1 
        if checkBoard(1) == 1:
            printBoard()
            print("Player 1 won!")
            break
        printBoard()
        player2 = int(input("Please input the space number you would like to player your O "))
        board[player2] = 2
        if checkBoard(2) == 2:
            printBoard()
            print("Player 2 won!")
            break
    else:
        print("Draw!")
        break
