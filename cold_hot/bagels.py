import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    '''Генерирует строку уникальных цифр, длиной NUM_DIGITS'''
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    '''Подсказка'''
    if guess == secretNum:
        return 'Win!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot')
        elif guess[i] in secretNum:
            clues.append('Warm')
    if len(clues) == 0:
        return 'Cold'

    clues.sort()
    return ' '.join(clues)


def isOnlyDigits(num):
    '''Если строка состоит из цифр - True, иначе False'''
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
        return True


print(f'Guess the number len {NUM_DIGITS}')
print('if I say: \nCold - not guess'
      '          \nWarm - guess the number, but not position'
      '          \nHot - guess the number and position')

while True:
    secretNum = getSecretNum()
    print(f'Now, I guess the number. You have {MAX_GUESS} try')

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print(f'Try №{guessesTaken}')
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print(f'You have no tries. I guess the number {secretNum}')

    print('Play again? (y or n)')
    if not input().lower().startswith('y'):
        break
