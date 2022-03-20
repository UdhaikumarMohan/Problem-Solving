#Find the Square of the given number:

#User Input:

N = (eval(input("Enter the number: ")))

#Define the function:
def Squ(N):

#Here we use exception handling to counter string values:
    try:
        print("Welcme user.....")
        Square = pow(N, 2)
        print("Square of the given number is: ", Square)

    except TypeError as t:

        print("Given value is not a number -->", t)

    finally:
        print("Thank you user....")

#Call the function to execute the program:
Squ(N)

#Why exception handling:

#Here we can square only integers and floats, by using exception handling we can counter the string values:
