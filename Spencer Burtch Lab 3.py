def getlettergrade(examscore):
    #Checking if the the inputted exam score is between the range of 0 and 100. If not, print an error message and return None.
    if examscore < 0 or examscore > 100:
        print("Error: The exam score must be between 0 and 100.")
        return None
    #If, elif, and else statement for determinging what inputted exam score is and returning the letter grade
    if examscore >= 90:
        return "A"
    elif examscore >= 80: 
        return "B"
    elif examscore >= 70:
        return "C"
    elif examscore >= 60:
        return "D"
    else:
        return "F"

#Defining examscore and lettergrade.
examscore = float(input("Enter your exam score from 0 to 100: "))
lettergrade = getlettergrade(examscore) 

#Print function to print the letter grade if it is not None.
#Float turns the inputted exam score into a number so it can be ran through the getlettergrade function.

if lettergrade is not None:
    print(f"Your letter grade is {lettergrade}.")

  