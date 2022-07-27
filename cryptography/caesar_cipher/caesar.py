#!/usr/bin/python

'''
CLI program to encrypt or decyprt text documents using Caesar cipher.

    ./caesar.py file.txt -m encrypt/decrypt -s numer_of_shifts [-o output.txt]

If there's no output, the text is printed on the terminal.

'''

import argparse
from method_modules import encrypt, decrypt


parser = argparse.ArgumentParser(description='Encrypt or decrypt a document using Caesar chipher.')

parser.add_argument('input',
                    help='input file.')
parser.add_argument('-m', '--method',
                    metavar='ENCRYPT/DECRYPT',
                    required=True)
parser.add_argument('-s', '--shift',
                    help='number of shifts to the left.',
                    metavar='0-53',
                    type=int,
                    required=True)
parser.add_argument('-o', '--output',
                    metavar='output.tx')

args = parser.parse_args()

if args.method == 'encrypt':
    TEXT = str()

    with open(args.input) as file:
        for lines in file:
            TEXT = TEXT + lines

    etext = encrypt(TEXT, args.shift)

    if not args.output:
        print(etext)
    else:
        with open(args.output, 'w') as outfile:
            outfile.write(etext)

elif args.method == 'decrypt':
    TEXT = str()

    with open(args.input) as file:
        for lines in file:
            TEXT = TEXT + lines

    dtext = decrypt(TEXT, args.shift)

    if not args.output:
        print(dtext)
    else:
        with open(args.output, 'w') as outfile:
            outfile.write(dtext)
else:
    print("Invalid input: argument -m/--method must be 'encrypt' or 'decrypt'\n")
