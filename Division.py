#Find the Quotient and Remainder of the given Numerator and Denominator.
#Numerator(N), Denominator(D), Quotient(Q), Remainder(R)

#Define function:

def div(N, D):

#Here we use exception handling to counter the zero divisible error:
    try:
        N = int(N)
        D = int(D)
        Q = N//D
        R = N%D

        print("Quotient: ", Q)
        print("Remainder: ", R)
    
    except ValueError as v:
        Q = v
        R = v
        print(Q)
        print(R)
        print("Invalid input, only integers are allowed")

    except ZeroDivisionError as z:
        Q = z
        R = z
        print(Q)
        print(R)
        print("Anything divided by zero is Infinity")

#User Input:
N = input("Enter the value of Numerator: ")
D = input("Enter the value of Denominator: ")

#Call the function:
div(N, D)

