# Value of (a) raised to the power of (b), use pow() fuction.
# (a) and (b) are positive integers.

#Define fuction and get an input through it:
def Power_func(a, b):
# c is just a variable name:
    c = pow(b,a)
    print("The value of a raised to the power of b is: ", c)

#User Input:
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

#Call the function:
Power_func(a,b)