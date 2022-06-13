#Perimeter of the circle with given radius(r).

#Here import the module math for the constant pi:
import math

#Define the function:
def Circ(r):

#Write conditions to prevent negative values:
    if (r>=0):
#Use the mathematical formula here:
        Perimeter = (2*(math.pi)*r)
        print("The perimeter of the given Circle is %.4f" %Perimeter)
    else:
        print("Negative integers are not allowed please give a valid Input....") 

#User Input:
r = float(input("Enter the Radius of the Circle: "))

#Calling the Function
Circ(r)

