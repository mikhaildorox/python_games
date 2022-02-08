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
        print(f'|{y + 1}')
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
    #  return True if coord in board
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def getBoardWithValidMoves(board, tile):
    # return new board with help
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy


def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enterPlayerTile():
    # Player can move. return tile player and comp tile
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do yo want to play with X or O?')
        tile = input().upper()

    # first tile for player, second for comp
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Comp'
    else:
        return 'Human'


def makeMove(board, tile, xstart, ystart):
    #  put tile in position xstart, ystart, reverse tile opponent
    # return False if incorrect move, else True
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]
    return boardCopy


def isOnCorner(x, y):
    # True if position in the corner
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def getPlayerMove(board, playerTile):
    #  return Move or help or exit
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('write move or help or exit')
        move = input().lower()
        if move == 'exit' or move == 'help':
            return move
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Incorrect move. Column (1-8), String (1-8)')
            print('For example 81 top-left corner')
    return [x, y]


def getComputerMove(board, computerTile):
    #  Scan the board and think where put tile
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    #  move in the corner high priority
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    #  Get move with more score
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
        return bestMove


def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print(f'Your score: {scores[playerTile]}. Comp score: {scores[computerTile]}.')


def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn + ' goes first')

    #  clean board and put start tiles
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)
        if playerValidMoves == [] and computerValidMoves == []:
            return board  # Moves is done
        elif turn == 'Human':
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'exit':
                    print('Thanks for the game!')
                    sys.exit()
                elif move == 'help':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'Comp'
        elif turn == 'Comp':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)
                input('Enter for show comp move')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'Human'


print('Welcome in The Reverse!')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    # Final Score
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X have %s scores. O have %s scores.' %(scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print(f'You WIN and have more scores about {scores[playerTile] - scores[computerTile]}')
    elif scores[playerTile] < scores[computerTile]:
        print(f'You LOSE and comp have more scores about {scores[computerTile] - scores[playerTile]}')
    else:
        print('Draw')


    print('One more times? (y or n)')
    if not input().lower().startswith('y'):
        break