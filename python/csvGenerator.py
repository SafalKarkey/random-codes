import random

def randomGenerator(n):
    randomFile = open("numbers.csv", "w")
    for i in range(n):
        randomFile.write(str(random.randint(0, 100)))
        if( i < n-1):
            randomFile.write(',')

def main():
    n = input("Enter number of integers to generate: ")
    randomGenerator(int(n))

if __name__ == "__main__":
    main()