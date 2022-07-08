# 1. Program to Check if a Number is Positive, Negative or 0
# 2. Check if two integers are equal or not
# 3. Check if two floating point numbers are equal or not
# 4. Program to Check if a Number is Odd or Even

# Enter the Input from the user:
N = eval(input("Enter the Number: "))
Integer1 = int(input("Enter the Integer1: "))
Integer2 = int(input("Enter the Integer2: "))
Float1 = float(input("Enter the Float1: "))
Float2 = float(input("Enter the Float2: "))

# Positive or Negative numbers.

def Number(N):

    if (N>0):
        print("The given number is positive number.")

    elif (N==0):
        print("This is Zero.")

    else:
        print("The given number is negative number.")

# Two integers.

def Integers(Integer1,Integer2):

    if (Integer1==Integer2):
        print("The given integers are equal.")

    else:
        print("The given integers are not equal.")

# Two floating point numbers.

def Floats(Integer1,Integer2):

    if (Float1 == Float2):
        print("The given Floating points are equal.")

    else:
        print("The given Floating points are not equal.")

# Odd or even:

def OE(N):

    if (N>0):

        if (N%2==0):
            print("The given number is even.")

        else:
            print("The given number is odd.")

    else:
        print("The given nuber is zero or negative number.")

# Now call the functions under the main function to execute the above codes.

def main():

    Number(N)
    Integers(Integer1, Integer2)
    Floats(Float1, Float2)
    OE(N)

main()