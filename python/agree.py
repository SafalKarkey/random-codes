agreed = True

while agreed:
    phrase = input("Do your agree?: ")
    if phrase.lower() in ["y", "yes", "agreed", "agree"]:
        print("Your agreed!")
    elif phrase.lower() in ["n", "no", "disagreed", "disagree"]:
        print("You disagreed!")
        agreed = False
    else:
        print("Invalid choice")