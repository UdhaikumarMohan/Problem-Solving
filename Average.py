# Get the three integer as a user input and find their average:

# Get input form user:
I_1 = int(input("Enter the Integer 1: "))
I_2 = int(input("Enter the Integer 2: "))
I_3 = int(input("Enter the Integer 3: "))

# Define the function:
def Average(I_1, I_2, I_3):

    if (I_1>=0) and (I_2>=0) and (I_3>=0):
        Avg = (I_1+I_2+I_3)/3
        print("The average of given three integers are: %.3f" %Avg)
    else:
        print("Negative Integers are not allowed.")

# Call the function:
Average(I_1, I_2, I_3)