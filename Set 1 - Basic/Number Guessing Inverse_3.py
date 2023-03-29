

# # System guessing the number given by user. (Using Binary Search)

Range = int(input("Enter the Range: "))

MagicNumber = int(input("Enter the Magic Number: "))

def Numguess_inv(Range, MagicNumber):

    if MagicNumber>=0 and MagicNumber<=Range:

        Attempts = 1
        Min = 0
        Max = Range
        Guess = (Min+Max)//2

        while MagicNumber!= Guess:

            if Guess > MagicNumber:
                Max = Guess
                print(Guess, "is greater than Magic Number")

            elif Guess < MagicNumber:
                Min = Guess
                print(Guess, "is lesser than Magic Number: ")
            
            Attempts+=1
            Guess = (Min+Max)//2

        print(Guess, "Bingo...!")
        print(Attempts, "attempts taken to find the Magic Number.")

    else:
        print(MagicNumber,"is out of range")

Numguess_inv(Range, MagicNumber)