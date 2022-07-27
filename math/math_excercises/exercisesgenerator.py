import random
import sys
import tty
import termios

def getchr(prompt=''):
    """reads a single character"""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def operation(first_num, second_num, operator):
    """takes the operation string and numbers and return the answer"""

    if operator == '+':
        return(first_num + second_num)
    elif operator == '-':
        return(first_num - second_num)
    elif operator == 'x':
        return(first_num * second_num)
    elif operator == '/':
        return(first_num / second_num)
    else:
        sys.exit("Error, exiting")


if __name__ == "__main__":
    operators = ['+', '-', 'x', '/']

    num_one, num_two = random.randint(1,1000), random.randint(1, 1000)
    operator = random.choice(operators)

    print(f'{num_one}{operator}{num_two}')
    print(getchr("press any key to show the answer"))

    print(operation(num_one, num_two, operator))
