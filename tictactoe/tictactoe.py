"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

BOARD_SIZE = 3

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    Always starting with X
    """
    all_empty = all(cell == EMPTY for row in board for cell in row)
    xs = sum(cell == X for row in board for cell in row)
    os = sum(cell == O for row in board for cell in row)
    return X if all_empty or xs == os else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Can't execute movement. Cell is already filled")
    nextPlayer = player(board)
    board[i][j] = nextPlayer
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return checkRowsWin(board) or checkColsWin(board) or checkDiagonalWin(board) or checkAntiDiagonalWin(board) or checkTie(board)


def checkRowsWin(board):
    """
    Returns True if X or O completed a whole row (and won)
    """
    xs_per_row = [sum(cell == X for cell in row) for row in board]
    os_per_row = [sum(cell == O for cell in row) for row in board]
    return any(count == BOARD_SIZE for count in xs_per_row) or any(count == BOARD_SIZE for count in os_per_row)


def checkColsWin(board):
    """
    Returns True if X or O completed a whole column (and won)
    """
    xs_per_col = [sum(board[row][col] == X for row in range(len(board))) for col in range(BOARD_SIZE)]
    os_per_col = [sum(board[row][col] == O for row in range(len(board))) for col in range(BOARD_SIZE)]
    return any(count == BOARD_SIZE for count in xs_per_col) or any(count == BOARD_SIZE for count in os_per_col)


def checkDiagonalWin(board):
    """
    Returns True if X or O completed the diagonal (and won)
    """
    xs = sum(board[i][i] == X for i in range(BOARD_SIZE))
    os = sum(board[i][i] == O for i in range(BOARD_SIZE))
    return xs == BOARD_SIZE or os == BOARD_SIZE


def checkAntiDiagonalWin(board):
    """
    Returns True if X or O completed the antidiagonal (and won)
    """
    xs = sum(board[i][BOARD_SIZE - 1 - i] == X for i in range(BOARD_SIZE))
    os = sum(board[i][BOARD_SIZE - 1 - i] == O for i in range(BOARD_SIZE))
    return xs == BOARD_SIZE or os == BOARD_SIZE


def checkTie(board):
    """
    Returns True if all cells are filled and the games ended in a tie
    """
    return all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
