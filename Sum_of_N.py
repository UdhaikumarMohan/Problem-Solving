# Find the sum of Naturaal Numbers upto N. (Hint: (N(N+1))/2)

# User Input:
N = int(input("Enter the Number: "))

# Define the fuction:
def Sum_Number(N):
    if N>0:
        Sum_of_N = (N*(N+1))//2
        result = Sum_of_N
    else:
        result = "Natural number should not be less than one"

    return(result)

# Call the function to execute the program.
print("The sum of natural number upto " + str(N) + " is: ", Sum_Number(N) )