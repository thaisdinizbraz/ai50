"""
Tic Tac Toe Player
"""

import math
import copy

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
    return {
        (i, j)
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if cell == EMPTY
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if not (0 <= i < BOARD_SIZE and 0 <= j < BOARD_SIZE):
        raise Exception(f"Can't execute movement. Action ({i}, {j}) is out of bounds")

    if board[i][j] != EMPTY:
        raise Exception("Can't execute movement. Cell is already filled")

    newBoard = copy.deepcopy(board)
    nextPlayer = player(board)
    newBoard[i][j] = nextPlayer
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return {1: X, -1: O}.get(utility(board), None)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (
        checkRowsWin(board) is not None or
        checkColsWin(board) is not None or
        checkDiagonalWin(board) is not None or
        checkAntiDiagonalWin(board) is not None or
        checkTie(board)
    )


def checkRowsWin(board):
    """
    Returns X or O if a whole row is completed
    """
    for row in board:
        if all(cell == X for cell in row):
            return X
        if all(cell == O for cell in row):
            return O
    return None


def checkColsWin(board):
    """
    Returns X or O if a whole column is completed
    """
    for col in range(BOARD_SIZE):
        if all(board[row][col] == X for row in range(BOARD_SIZE)):
            return X
        if all(board[row][col] == O for row in range(BOARD_SIZE)):
            return O
    return None


def checkDiagonalWin(board):
    """
    Returns X or O if the diagonal is completed
    """
    if all(board[i][i] == X for i in range(BOARD_SIZE)):
        return X
    if all(board[i][i] == O for i in range(BOARD_SIZE)):
        return O
    return None


def checkAntiDiagonalWin(board):
    """
    Returns X or O if the antidiagonal is completed
    """
    if all(board[i][BOARD_SIZE - 1 - i] == X for i in range(BOARD_SIZE)):
        return X
    if all(board[i][BOARD_SIZE - 1 - i] == O for i in range(BOARD_SIZE)):
        return O
    return None


def checkTie(board):
    """
    Returns True if all cells are filled and the games ended in a tie
    """
    return all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ans = (
        checkRowsWin(board)
        or checkColsWin(board)
        or checkDiagonalWin(board)
        or checkAntiDiagonalWin(board)
    )
    return {X: 1, O: -1}.get(ans, 0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentPlayer = player(board)
    if currentPlayer == X:
        _, action = maxValue(board)
    else:
        _, action = minValue(board)
    return action


def maxValue(board):
    if terminal(board):
        return utility(board), None
    value = float('-inf')
    bestAction = None
    for action in actions(board):
        minVal, _ = minValue(result(board, action))
        if (minVal > value):
            value = minVal
            bestAction = action
    return value, bestAction


def minValue(board):
    if terminal(board):
        return utility(board), None
    value = float('inf')
    bestAction = None
    for action in actions(board):
        maxVal, _ = maxValue(result(board, action))
        if (maxVal < value):
            value = maxVal
            bestAction = action
    return value, bestAction