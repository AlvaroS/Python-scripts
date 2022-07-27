import sys

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False

    return True

def main():
    try:
        number = sys.argv[1]
    except IndexError:
        print("Please write a number as an argument")
        sys.exit()

    if is_prime(int(number)):
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

if __name__ == "__main__":
    main()
