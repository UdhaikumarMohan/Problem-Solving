# Find the area of triangle using given base and height.
# Area of triangle = (1/2x(b.h))

# User Input:
base = eval(input("Enter the base of the triangel in Meters: "))
height = eval(input("Enter the height of the triangle in Meters: "))

# Define function with base and height as an arguments.
def Area_of_triangle(base, height):

# Now we use exception handling to counter string inputs
    try:
        print("Welcome user....")

        if (base>=0) and (height>=0):
            Area = ((1/2)*(base*height))
            print("Area of the triangle is %.3f" %Area + " m^2")
        else:
            print("Negative values are not allowed")

    except ValueError as v:
        print("Given values are not real numbers -->", v)

    finally:
        print("Thank you user....")

# Call the function to excecute the program:
Area_of_triangle(base, height)


