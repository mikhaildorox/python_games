# Крестики-нолики

import random


def drawBoard(board):
    """Create board when add X or O"""
    # "board" - это список из 10 строк, для прорисовки поля индекс 0 игнорируется.
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'- + - + -')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'- + - + -')
    print(f'{board[1]} | {board[2]} | {board[3]}')


def inputPlayerLatter():
    # Choise X or O
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Выберите Х или О')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    """Random choise who first"""
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Human'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))
