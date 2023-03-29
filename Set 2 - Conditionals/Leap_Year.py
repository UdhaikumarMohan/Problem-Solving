# 5. Check the given year is Leap year or not

# Conditions for Leap year.

# Leap year:
# * The given year should be divided by 4 and it should not divied by 100.
# * The given year should be dived by 4, 100, 400.

# Not Lear year:
# * The given year is not divided by 4.
# * The given integer is dived by 4 and 100 but not divided by 400.

# Get the input from the user:


Year = int(input("Enter the year: "))

# Define the fuction.
def Leap_Year(Year):

# Create the Flag:
    Flag = False

# Negative integers are not allowed in this program.
    if (Year>0):

        # First condition of being leap year: Year should be divided by 4, 100, 400 without remainder
        if (Year%400==0):
            Flag = True
        
        # Second condition of being lear year: Year should be divided by 4 and not divided by 100:
        elif ((Year%4==0) & (Year%100!=0) ):
            Flag = True

        # Otherwise the given year is not a leap year and flag remains False.
        else:
            Flag = False

    else:
        Flag = "The given year is not a valid year."

    return Flag

# Now execute the above function with print statements using the new function.

def Execution():

    if (Leap_Year(Year) is True):
        print ("The given year is Leap year")
    elif (Leap_Year(Year) is False):
        print ("The given year is not a Leap year")
    else:
        print (Leap_Year(Year))

Execution()

