"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    """
    x = 0
    o = 0
    for row in board:
        for pos in row:
            if pos == "X":
                x += 1
            if pos == "O":
                o += 1
    return X if x == o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                pos.append((row, col))
    return pos


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("position already occupied")
    new = copy.deepcopy(board)
    new[i][j] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row == [X, X, X]:
            return X
        elif row == [O, O, O]:
            return O
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if col == [X, X, X]:
            return X
        elif col == [O, O, O]:
            return O
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]
    if diag1 == [X, X, X] or diag2 == [X, X, X]:
        return X
    elif diag1 == [O, O, O] or diag2 == [O, O, O]:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     turn = player(board)
#     moves = actions(board)
#     if turn == X:
#         v = min_value(board)
#     elif turn == O:
#         move = max_value(board)
#     return move


def get_max(v):
    ix = 0
    maxV = v[0]
    for i, x in enumerate(v):
        if x > maxV:
            ix, maxV = i, x
    return ix


def get_min(v):
    ix = 0
    minV = v[0]
    for i, x in enumerate(v):
        if x < minV:
            ix, minV = i, x
    return ix


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X : Max
    O : Min
    """
    if terminal(board):
        return None

    moves = actions(board)
    turn = player(board)
    v = []
    if turn == X:  # Max
        for action in moves:
            v.append(min_value(result(board, action)))
        return moves[get_max(v)]
    elif turn == O:  # Min
        for action in moves:
            v.append(max_value(result(board, action)))
        return moves[get_min(v)]

# def min_value(board):
#     v = float("-inf")
#     score = {}
#     if terminal(board):
#         return utility(board)
#     for action in actions(board):
#         v_prime = max_value(result(board, action))
#
#         if v > v_prime:
#             v = v_prime
#             move = action
#     return move
#
#
# def max_value(board):
#     v = float("inf")
#     move = None
#     if terminal(board):
#         return utility(board)
#     for action in actions(board):
#         v_prime = min_value(result(board, action))
#         if v < v_prime:
#             v = v_prime
#             move = action
#     return move
