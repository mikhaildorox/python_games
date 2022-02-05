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


def getRandomChests(numChests):
    # Create chest (coord x and y)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
    if newChest not in chests:  # to prove for chest was created
        chests.append(newChest)
    return chests


def isOnBoard(x, y):
    # return True if coord on board, else False
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


def makeMove(board, chests, x, y):
    # Изменить структуру данных поля, используя символ гидролокатора. Удалить сундуки
    # с сокровищами из списка сундуков, как только их нашли. Вернуть False, если это
    # недопустимый ход. В противном случае, вернуть строку с результатом этого хода.
    smallestDistance = 100  # all chests in distance < 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
            smallestDistance = distance

        smallestDistance = round(smallestDistance)

        if smallestDistance == 0:
            # find the chest
            chests.remove([x, y])
            return 'You find the treasure!'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return f'find treasure in distance {smallestDistance}'
            else:
                board[x][y] = 'X'
                return 'nothing'

def enterPlayerMove(previousMove):
