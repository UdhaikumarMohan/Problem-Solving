
# User Guessing the System generated number.

import random

Range = int(input("Enter the Range: "))
MagicNumber = random.randint(1, Range+1)

def NumGuess(MagicNumber):

    Attempts = 1
    Guess = int(input("Guess your Answer: "))
    while Guess != MagicNumber:

        if Guess<0 or Guess>Range:
            print("Your Guess is out of Range, Please provide your Guess in between 0 and ", Range)

        elif Guess < MagicNumber:
            print(Guess, "Your Guess is lesser than Magic Nummber ")

        elif Guess > MagicNumber:
            print(Guess, "Your Guess is greater than MagicNumber ")

        Attempts+=1
        Guess = int(input("Guess your Answer: "))
    print(Guess, "Bingo...!")
    print("Magic Number: ", MagicNumber)
    print("Number of Attempts to Guess: ", Attempts)

NumGuess(MagicNumber)
    