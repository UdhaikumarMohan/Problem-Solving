# Swap two variables with and without using temp variable and without causing overflow

# User Input:
A = eval(input("Enter the value of A: "))
B = eval(input("Enter the value of B: "))

# Define the function for first code (swap with temp variable)
def Swap_1(A, B):
    Temp = A
    A = B
    B = Temp
    print("A: ", A)
    print("B: ", B)

# Define the function for second code (swap without temp variable)
def Swap_2(A, B):
    A,B = B,A
    print("A: ", A)
    print("B: ", B)

# Define the function for third code (swap without causing overflow)
def Swap_3(A, B):
    A = A ^ B
    B = A ^ B
    A = A ^ B
    print("A: ", A)
    print("B: ", B)

# Call the functions:
Swap_1(A, B)
Swap_2(A, B)
Swap_3(A, B)