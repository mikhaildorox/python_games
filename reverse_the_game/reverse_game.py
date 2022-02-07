# Reverse It`s Otello

import random
import sys

WIDTH = 8  # board have 8 cells in width
HEIGHT = 8  # board have 8 cells in height


def drawBoard(board):
    #  draw board. Return nothing
    print('  12345678')
    print(' +---------+')
    for y in range(HEIGHT):
        print(f'{y + 1}|', end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
    print(' +---------+')
    print('  12345678')


def getNewBoard():
    #  Create structure for new clean board
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def isValidMove(board, tile, xstart, ystart):
    #  Return False if move not correct
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection  # first move on x
        y += ydirection  # first move on y
        while isOnBoard(x, y) and board[x][y] == otherTile:
            #  move in this direction
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                #  if have tiles for revers - move on back and check all this tiles
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
        if len(tilesToFlip) == 0:  # if no one tiles not flipped it`s not correct move
            return False
    return tilesToFlip


def isOnBoard(x, y):
    pass


def getBoardWithValidMoves(board, tile):
    pass


def getValidMoves(board, tile):
    pass


def getScoreOfBoard(board):
    pass


def enterPlayerTile():
    pass


def whoGoesFirst():
    pass


def makeMove(board, tile, xstart, ystart):
    pass
