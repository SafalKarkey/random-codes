#dictionary = {"key1" : "value1", .....}
#Dictionary is like a hash-table
#enter name from command line to search name in phonebook
#python phonebook.py *name*
import sys

def argcheck():
    if len(sys.argv) < 2:
        print("Incomplete arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many parameters")
        sys.exit(2)

def searchName(phonebook):
    name = sys.argv[1]
    
    if name in phonebook:
        print(f"\n{name}'s number: {phonebook[name]}")
    
    else:
        print("\nName not found in phonebook")

def main():
    phonebook = {"Peter":"123456778", "Lois":"987654321", "Stewie": "456789123", "Brian":"345678912", "Joe":"567891234"}
    argcheck()
    searchName(phonebook)

if __name__ == "__main__":
    main()
