'''
Functions to encrypt or decrypt a message using Caesar cipher.

Functions:

    encrypt(message, key)
    encrypt(message) -> string
    encrypt(key) -> integrer

    decrypt(message, key)
    decrypt(message) -> string
    decrypt(key) -> integrer

'''

def encrypt(msg, key):
    '''Enter a message and encrypt it the number of shifts in key'''

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

def decrypt(msg, key):
    '''Enter an encrypted message and decrypt it the number of shifts in key'''

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
