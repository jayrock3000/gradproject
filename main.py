#################################################################################
# Necessary import statements, helper functions, and global variables

import globalVariables
DEBUG = globalVariables.DEBUG


#################################################################################
# Function for handling user inputs of strings

def stringInput(prompt, minLength, maxLength):
    userInput = ""

    while True:
        print(prompt, end="")
        userInput = input()
        try:
            userInput = str(userInput)
        except:
            print("Sorry, it looks like that wasn't a valid entry. Please try again.\n")
            continue
        if userInput == "":
            print("Entry cannot be blank\n")
            continue

        elif len(userInput) < minLength:
            print("Sorry, minimum number of characters is " + str(minLength) + "\n")
            continue

        elif len(userInput) > maxLength:
            print("Sorry, maximum number of characters is " + str(maxLength) + "\n")
            continue
        break
    return userInput


#################################################################################
# Function for handling user inputs of integers

def intInput(prompt, minInt, maxInt):
    userInput = minInt - 1

    while True:
        print(prompt, end="")
        userInput = input()
        try:
            userInput = int(userInput)
        except:
            print("Entry must be a whole number.\n")
            continue
        if userInput < minInt:
            print("Sorry, minimum value is " + str(minInt) + "\n")
            continue
        elif userInput > maxInt:
            print("Sorry, maximum value is " + str(maxInt) + "\n")
            continue
        break
    return userInput


#################################################################################
# Function for writing main menu options to the console

def displayMainMenu():
    print("\nMain Menu\n")
    print("1. WIP")
    print("2. WIP")
    print("3. WIP")
    print("4. Exit\n")


#################################################################################
# Main program loop

def main():

    print("_______________________")
    print("")
    print("Jeffrey Rhoten")
    print("CSUF Graduate Project")
    print("6/18/2025")
    print("_______________________")

    if(DEBUG):
        print("Debug mode is ON")

    selection = -1
    prompt = "Your selection: "
    skipNum = 0
    
    while selection != 4:
        displayMainMenu()
        
        selection = intInput(prompt, 1, 4)

        if DEBUG:
            print(f"\nSelection received ({selection})")

        if selection == 1:
            print("***WIP***")

        elif selection == 2:
            print("***WIP***")

        elif selection == 3:
            print("***WIP***")
        
        elif selection == 4:
            break
    
    print("\n\nThank you, take care!\n\n")
    exit()


#################################################################################
# Initialize main

if __name__ == "__main__": main()