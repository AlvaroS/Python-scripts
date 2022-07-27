def encrypt(msg, key):
    symbols = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    translated = str()

    for letter in msg:
        if letter in symbols:
            index = symbols.find(letter) + key
        else:
            translated = translated + letter
            continue

        if index >= len(symbols):
            index = index - len(symbols)

        translated = translated + symbols[index]

    return translated
