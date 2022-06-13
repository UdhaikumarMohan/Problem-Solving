# Find the Square root of the given number: Hint (Use sqrt() function.)
# eval(input()) used to take different data types. input() function will read input as only string.
# import math library to access sqrt() function.

from math import sqrt

# User Input:
N = eval(input("Enter the Number: "))

# Now Define the function:
def Square_root(N):

# Use exception handling to deal with string inputs:
    try:
        print("Welcome user....")
        Root = sqrt(N)
        print("The Square root of the given number is %.3f" %Root)

    except TypeError as t:
        print("The given value is not a number -->", t)

    finally:
        print("Thank you user....")

#Call the function:
Square_root(N)


