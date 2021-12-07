import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
     |
      |
      |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

words = 'аист акулв бабуин баран бобр бык верблюд волк воробей выдра голубь гусь жаба зебра змея индюк кит кобра ' \
        'казел койот корова крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул ' \
        'муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс ' \
        'собака сова тигр тритон тюлень утка форель хорек черепаха ястеб ящерица'.split()


def getRandomWord(wordList):
    """Эта функция возвращает случайную строку из переданного списка"""
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # замена пропуска отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # показ секретного слова с пробелами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    '''bla-bla-bla'''
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву, назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def playAgain():
    """Эта функция возвращает True, ели игрок хочет сыграть"""
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяет выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'ДА! Секретное слово - "{secretWord}"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Превысил ли игрок лимит попыток?
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(
                f'Вы исчерпали все попытки! \n'
                f'Неугадано букв:{str(len(missedLetters))} и угадано букв:{str(len(correctLetters))}. \n'
                f'Было загадано слово {secretWord}.')
            gameIsDone = True

    # Сыграть снова?
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
