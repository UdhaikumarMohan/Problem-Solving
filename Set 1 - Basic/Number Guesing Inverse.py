
# System guessing the number given by user. (Using random)

import random
Range = int(input("Enter the Range of Guessing: "))

MagicNumber = int(input("User Please Provide the Magic Number: "))

def Numguess_inv(Range, MagicNumber):

    if MagicNumber >=0 and MagicNumber<=Range:

        Attempts = 1
        Sys_Guess = random.randint(0, Range+1)

        while Sys_Guess != MagicNumber:

            if Sys_Guess < MagicNumber:

                print (Sys_Guess, "Lesser than Magic Number")

            elif Sys_Guess > MagicNumber:

                print(Sys_Guess, "Greater than Magic Number")

            Attempts+=1
            Sys_Guess = random.randint(0, Range+1)

        print(Sys_Guess, "Bingo...!")
        print(Attempts, "attempts taken to Guess")

    else:
        print("The Given Input is out of Range")

Numguess_inv(Range, MagicNumber)


