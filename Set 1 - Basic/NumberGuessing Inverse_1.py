
# System guessing the number given by user. (Using random and changing range)

import random
Range = int(input("Enter the Range of Guessing: "))

MagicNumber = int(input("User Please Provide the Magic Number: "))

def Numguess_inv(Range, MagicNumber):

    if MagicNumber >=0 and MagicNumber<=Range:

        Attempts = 1
        min = 0
        max = Range
        Sys_Guess = random.randint(min, max)

        while Sys_Guess != MagicNumber:

            if Sys_Guess < MagicNumber:

                print (Sys_Guess, "Lesser than Magic Number")
                min = Sys_Guess+1

            elif Sys_Guess > MagicNumber:

                print(Sys_Guess, "Greater than Magic Number")
                max = Sys_Guess-1

            Attempts+=1
            Sys_Guess = random.randint(min, max)

        print(Sys_Guess, "Bingo...!")
        print(Attempts, "attempts taken to Guess")

    else:
        print("The Given Input is out of Range")

Numguess_inv(Range, MagicNumber)


