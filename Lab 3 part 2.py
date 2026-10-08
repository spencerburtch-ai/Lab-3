def stripSpaces(myString):
    newString = ""

    for character in myString:
        if character != " ":
            newString += character

    return newString


phrase = input("Enter a phrase: ")
print(stripSpaces(phrase))

                                