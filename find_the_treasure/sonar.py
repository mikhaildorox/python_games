# Treasure hunter

import random
import sys
import math


def getNewBoard():
    # New board 60x15
    board = []
    for x in range(60):
        board.append([])
    for y in range(15):
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
    return board


def drawBoadr(board):
    # Draw new board
    tensDigitsLine = ' '  # Create places for digits down in left side board
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # print digits in top side on board
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # print 15 column
    for row in range(15):
        # digits need whitespace
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

    # create srting for this column in board
    boardRow = ''
    for column in range(60):
        boardRow += board[column][row]

    print(f'{extraSpace}, {row}, {boardRow}, {row}')

    # print digits in bottom side on board
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)
