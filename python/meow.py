import time

def main():
    start = time.time()
    meow()
    end = time.time()
    print(f"\n{end - start}")
    

def meow():
    num = int(input("How many meow?: "))

    file = open("meow.txt", "w")
    for i in range(num):
        file.print(f"{i+1}. meaow")
    file.close()

if __name__ == "__main__":
    main()