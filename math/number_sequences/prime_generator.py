import sys

def is_prime(n):
    """If a number is prime return True, else False"""
    if n <= 1:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False

    return True

def numbers(number_range):
    """Check if numbers in a range and return the primes"""
    for i in range(1, number_range):
        if is_prime(i):
            yield i
        else:
            pass

def main():
    try:
        max_num = sys.argv[1]
    except IndexError:
        print("Please write a number as an argument")
        sys.exit()

    for number in numbers(int(max_num)):
        print(number)

if __name__ == "__main__":
    main()
