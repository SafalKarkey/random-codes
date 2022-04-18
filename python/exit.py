import sys

if len(sys.argv) < 2:
    print("Incomplete arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many parameters")
    sys.exit(2)

print(f"Your string is {sys.argv[1]}")
sys.exit(0)