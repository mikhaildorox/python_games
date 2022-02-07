# Chipher of Ceasar

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя 1234567890!"№;%:?*()@#$%^&,\/.'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Вы хотите зашифровать, расшифровать или взломать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в']:
            return mode
        else:
            print('Введите зашифровать или з для шифрования, или расшифровать или р для расшифровки,'
                  ' или в или взломать для взлома')


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
if mode[0] != 'в':
    key = getKey()
    print('Text was changed')
    if mode[0] != 'в':
        print(getTranslateMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslateMessage('расшифровать', message, key))
