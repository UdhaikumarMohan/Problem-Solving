#Find the Quotient and Remainder of the given Numerator and Denominator.
#Numerator(N), Denominator(D), Quotient(Q), Remainder(R)

#Define function:

def div(N, D):

#Here we use exception handling to counter the zero divisible error:
    try:
        Q = N//D
        R = N%D

    except ZeroDivisionError as z:
        Q = z
        R = z
        print("Anything divided by zero is Infinity")

    finally:
        print("Quotient: ", Q)
        print("Remainder: ", R)

#User Input:
N = int(input("Enter the Numerator value: "))
D = int(input("Enter the Denominator value: "))
#Call the function:
div(N, D)

