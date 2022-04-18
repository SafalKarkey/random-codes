import sys
import random

def argcheck():
    if len(sys.argv) < 2:
        print("Incomplete arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many parameters")
        sys.exit(2)


def insertint(numbers):
    for i in range(100):
        numbers.append(random.randint(0,10000))

    print(f"The numbers in list are: ")

    for i in range(100):
        print(numbers[i], end=" ")


def main():
    numbers = []
    argcheck()
    insertint(numbers)
    if sys.argv[1] in numbers:
        print(f"The number {sys.argv[1]} was found in list")
    else:
        print("\nNumber not found")

if __name__ == "__main__":
    main()