# Chipher of Ceasar

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите зашифровать или з для шифрования или расшифровать или р для расшифровки')


def getMessage():
    print('Введите текст:')
    return input()


def getKey():
    key = 0
    while True:
        print(f'Введите ключ шифрования (1 - {MAX_KEY_SIZE})')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslateMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # symbol not find
            translated += symbol  # add symbol
        else:
            symbolIndex += key  # chipher symbol
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
key = getKey()
print('Text was changed')
print(getTranslateMessage(mode, message, key))

