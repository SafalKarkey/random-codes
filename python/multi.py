i = 1

num = int(print("How many? "))

file = open("new.txt", "w")
for j in range(num):
    # i *= 2
    file.write(f"{i*2}")