import random
import operator

def question(first_operand, second_operand, question_operator):
    '''Get two numbers and an operator and return the answer and an user input'''
    operatorsdic = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
    }
    op = operatorsdic.get(question_operator)

    print(f"{first_operand} {question_operator} {second_operand}")

    while True:
        try:
            user_answer = int(input())
            break
        except ValueError:
            print("That is not a valid value, please try again")
            continue

    real_answer = op(first_operand, second_operand)

    return user_answer, real_answer

def main():
    '''Randomly generate 10 equations, compare the results with the user result and return a score.'''
    score = 0
    question_number = 0

    while question_number < 10:
        first_num = random.randint(1, 1000)
        second_num = random.randint(1, 100)
        operat = random.choice(["+", "-", "*", "/"])

        answer, result = question(first_num, second_num, operat)

        if answer == result:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong!, the correct anwser is {result}")

        question_number += 1

    print(f"You scored {score}/10")

if __name__ == "__main__":
    main()
