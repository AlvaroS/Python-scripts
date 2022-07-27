"""
Print all the numbers of the fibonacci secuence in a range defined by the user
"""
import sys

def fibonacci_secuence(integers_numbers):
    """ return all numbers of the fibonacci secuence """

    first_number, second_number = 0, 1

    for number in range(integers_numbers):
        first_number, second_number = second_number, first_number + second_number

        yield first_number


if __name__ == "__main__":
    try:
        MAX_NUM = int(sys.argv[1])
    except IndexError:
        MAX_NUM = 10

    for element in fibonacci_secuence(MAX_NUM):
        print(f'{element:,}')
