#!/bin/python

import sys

try:
    file = sys.argv[1]
except IndexError:
    print('Please enter a valid file name:\n\thacker.py file.txt')
    quit()

openfile= open(file)
text = str()

for line in openfile:
    text = text + line.rstrip()

symbols = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'

for i in range(len(symbols)):
    decoded = ''
    for letter in text:
        if letter in symbols:
            index = symbols.find(letter) - i
        else:
            decoded = decoded + letter
            continue

        if index > len(symbols):
            index = index + len(symbols)

        decoded = decoded + symbols[index]
    print(f'Key #{i}: {decoded}\n')
