'''
Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

the computer (i.e., your program) should play the game using 'X's;
the user (e.g., you) should play the game using 'O's;
the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
all the squares are numbered row by row starting with 1 (see the example session below for reference)
the user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
the program checks if the game is over - there are four possible verdicts: the game should continue, or the game ends with a tie, your win, or the computer's win;
the computer responds with its move and the check is repeated;
don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.
'''

from random import randrange
import time

statusGame = True

def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    selection = True
    while selection:
        move = int(input("Ingresa tu movimiento del tablero con el numero de una casilla vacia: "))
        if move < 1 or move > 9:
            continue
        if move not in MakeListOfFreeFields(board):
            print("La posicion que seleccionaste no esta disponible, por favor")
            continue
        else:
            if move > 0 and move < 4:
                board[0][move-1] = "O"
            elif move > 3 and move < 7:
                board[1][move-4] = "O"
            else:
                board[2][move-7] = "O"
            selection = False
    VictoryFor(board,"O")

def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    freeFields = ()
    for row in board:
        for data in row:
            if type(data) == int:
                freeFields += data,
            else:
                continue
    return freeFields

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #
    global statusGame
    player = None
    if sign == "X":
        player = True
        msg = "Perdiste, suerte para la proxima"
    else:
        player = False
        msg = "Ganaste, felicidades"
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign or \
        board[1][0] == sign and board[1][1] == sign and board[1][2] == sign or \
           board[2][0] == sign and board[2][1] == sign and board[2][2] == sign or \
           board[0][0] == sign and board[0][1] == sign and board[0][2] == sign or \
               board[0][0] == sign and board[1][1] == sign and board[2][2] == sign or \
                   board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: 
        DisplayBoard(board)
        print(msg)
        statusGame = False
    else:
        time.sleep(1)
        DisplayBoard(board)
        if player:
            EnterMove(board)
        else:
            DrawMove(board)


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    selection = True
    while selection:
        move = randrange(8)
        if move not in MakeListOfFreeFields(board):
            continue
        if move > 0 and move < 4:
            board[0][move-1] = "X"
        elif move > 3 and move < 7:
            board[1][move-4] = "X"
        else:
            board[2][move-7] = "X"
        selection = False
    VictoryFor(board,"X")
    

board = []
row = 3
column = 3
for i in range(column+1,row*column+2,column):
    board.append([x for x in range(i-column,i)])

DisplayBoard(board)
board[1][1] = "X"
VictoryFor(board, "X")