'''
TABLERO DE AJEDREZ
'''

EMPTY = "-"
ROOK = "ROOK"
BISHOP = "BISHOP"
KNIGHT = "KNIGHT"
KING = "KING"
QUEEN = "QUEEN"
PAWN = "PAWN"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP
board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT
board[0][4] = KING
board[0][3] = QUEEN
board[7][4] = KING
board[7][3] = QUEEN
for i in range(8):
    board[1][i] = PAWN
    board[6][i] = PAWN

print(board)