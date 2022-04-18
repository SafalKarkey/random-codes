#script to count number of males and females from csv file
import csv

def main():
    genders = {"M": 0, "F": 0}

    with open("freshman_kgs.csv", "r") as file: 
        reader = csv.reader(file)   #create a reader object which will iterate over lines of csv file
        next(reader)    #increment reader to skip first row of csv

        for row in reader:
            gender = row[0] #gender = first column of reader which is either M or F in file
            genders[gender] += 1
        
        
    for gender in genders:
        print(f"{gender}: {genders[gender]}")

if __name__ == "__main__":
    main()
