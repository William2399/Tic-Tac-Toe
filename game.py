import random

board = [' ' for i in range(10)]

def printBoard(b):
    print("\n")
    print(b[1] + ' | ' + b[2] + ' | ' + b[3])
    print('- - - - -') 
    print(b[4] + ' | ' + b[5] + ' | ' + b[6])
    print('- - - - -') 
    print(b[7] + ' | ' + b[8] + ' | ' + b[9])

def isValidChoice(move):
    if board[move] == ' ': return True
    else: return False

def inputMove(p, move):
    board[move] = p

def isFull(b):
    return False if b.count(' ') > 1 else True

def isWin(b, p):
    return ((b[1] == p and b[2] == p and b[3] == p) or 
    (b[4] == p and b[5] == p and b[6] == p) or
    (b[7] == p and b[8] == p and b[9] == p) or 
    (b[1] == p and b[4] == p and b[7] == p) or 
    (b[2] == p and b[5] == p and b[8] == p) or 
    (b[3] == p and b[6] == p and b[9] == p) or 
    (b[1] == p and b[5] == p and b[9] == p) or 
    (b[3] == p and b[5] == p and b[7] == p))

def user_Choice():
    while True:
        user_Move = input("\n Please select a spot to place your move (1-9): ")
        try:
            user_Move = int(user_Move)
            if user_Move > 0 and user_Move < 10:
                if isValidChoice(user_Move):
                    inputMove('X', user_Move)
                    break;
                else: print("Sorry, that spot is already taken!")
            else: print("Sorry, your choice is not in specified range of 1-9.")
        except: print("Please put in a valid number.")

def computer_Choice():
    moves = []
    for index, value in enumerate(board):
        if index != 0 and value == " ": moves.append(index)
    for i in ['O', 'X']:
        for j in moves:
            copyBoard = board[:]
            copyBoard[j] = i
            if (isWin(copyBoard, i)):
                return j
    if moves == []: return 0;
    else:
        computer_move = random.randrange(0, len(moves))
        return moves[computer_move]

def main(): 
    print("\n Welcome to Tic-Tac-Toe!")
    printBoard(board)

    while not(isFull(board)):
        if not (isWin(board, 'O')): user_Choice()
        else:
            print("\n The winner is the computer!")
            printBoard(board)
            break;
        if not (isWin(board, 'X')):
            computer_move = computer_Choice()
            if computer_move == 0:
                    print("\n The game is a tie!")
                    printBoard(board)
                    break;
            else:
                inputMove('O', computer_move)
                printBoard(board)
        else:
            print("\n The user is the winner!")
            printBoard(board)
            break;

main()
while True:
    user_selection = input("\n Do you wish to play again? (y/n): ")
    if user_selection.lower() == 'y':
        board = [' ' for i in range(10)]
        main()
    elif user_selection.lower() == 'n':
        print("\n Alright, thanks for playing!")
        break;
    else: print("\n Please input either y or n")