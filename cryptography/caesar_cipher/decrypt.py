def decrypt(msg, key):
    symbols = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    decoded = ''

    for letter in msg:
        if letter in symbols:
                index = symbols.find(letter) - key
        else:
            decoded = decoded + letter
            continue

        if index > len(symbols):
            index = index + len(symbols)

        decoded = decoded + symbols[index]

    return decoded
