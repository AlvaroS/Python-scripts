# Math related scripts

A collection of math-related scripts, including 2 mathematical exercise generators (addition, subtraction, multiplication, division), a fibonacci generator and a prime number list generator.

# Math excercise

## Mathtest

mathtest displays 10 math exercises and prompts the user to write down the answer, tells the user whether the answer is correct or incorrect, and displays the final score.

    $ python mathtest.py
    991 - 57
    2
    Wrong!, the correct anwser is 934
    149 * 27
    4023
    Correct!

## Excercisesgenerator

excercisesgenerator is the first version of the program, it only displays an exercise and shows the answer after users click on any key.
**The script requires termius so it's incompatible with windows.**

    $ python excercisesgenerator.py
    962-421
    press any key to show the answer
    541

---
# Numbers Sequences

## Fibonacci sequence

fibonacci_sequence displays a list of numbers in the fibonacci sequence selected by the user. To use it you type the program followed by the number of numbers you want to see, if you do not type any number the program displays by default the first 10 numbers of the sequence.

    $ python fibonacci_sequence.py 5
    python fibonacci_sequence.py  5
    1
    1
    2
    3
    5

## Is prime

is_prime receives a number and shows if it is prime or not, this script is a dependency of prime_generator.

    $ python is_prime.py 17
    The number 17 is prime

## Prime generator

prime_generator shows a list of prime numbers from 2 to the number selected by the user.

    $python prime_generator.py 19
    2
    3
    5
    7
    11
    13
    17