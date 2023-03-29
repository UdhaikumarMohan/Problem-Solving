

# System guessing the number given by user. (Using Linear Search)

Range = int(input("Enter the Range of Guessing: "))

MagicNumber = int(input("User Please Provide the Magic Number: "))

def Numguess_inv (Range, MagicNumber):

    if MagicNumber >= 0 and MagicNumber <= Range:

        Guess = 0
        Attempts = 1

        while Guess != MagicNumber:

            print(Guess, "The Guess is lesser than the Magic Number")
            Guess+=1
            Attempts+=1

        print(Guess, "Bingo...!")
        print(Attempts, "attempts taken  to guess Magic Number")

    else:
        print("The given Magic Number is out of range")

Numguess_inv(Range, MagicNumber)