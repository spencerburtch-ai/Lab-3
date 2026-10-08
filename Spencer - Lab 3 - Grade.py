def getlettergrade(examscore):
    if examscore < 0 or examscore > 100:
        print("Error: The exam score must be between 0 and 100.")
        return None
    #If statement for determing what inputted exam score is and returning the letter grade
    if examscore >= 90:
        return "A"
    if examscore >= 80: 
        return "B"
    if examscore >= 70:
        return "C"
    if examscore >= 60:
        return "D"
    return "F"

#Defining examscore and lettergrade.
examscore = float(input("Enter your exam score from 0 to 100: "))
lettergrade = getlettergrade(examscore) 
#Print function to print the letter grade if it is not None.
if lettergrade is not None:
    print(f"Your letter grade is {lettergrade}.")

 