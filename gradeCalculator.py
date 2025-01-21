def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        score = float(input("Enter score:"))

        if score > 1.0:
            grade = "Bad score"
        elif score < 0:
            grade = "Bad score"
        elif score >= .9:
            grade = "A"
        elif score >= .8:
            grade = "B"
        elif score >= .7:
            grade = "C"
        elif score >= .6:
            grade = "D"
        elif score < .6:
            grade = "F"

    except:
        grade = ("Bad score")
    
    print (grade)

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
