# Given the height of a person in cm print the height in feet and inches. (1 inch= 2.54 cms)

# Since the height of the person cannot be given in negative values, we should avoid it.

# In this program we are going to calculate height of the person in feet and inches.

# Get the input form user (Height of the person should be given in Centimeter.)
Given_Height = eval(input("Enter the height of the person in cm: "))

# Define the function:
def Height(Given_Height):

    # Exception Handling:
    try:
        if Given_Height > 0:
            Height_in_inch = (Given_Height*(1/2.54))
            Height_in_feet = (Height_in_inch*(1/12))
            result = "The given height ({0} cm) is equal to ({1} inch) or it can be said as ({2} feet). "
            print(result.format(Given_Height, Height_in_inch, Height_in_feet))

        else:
            print("Negative values are not allowed")

    except Exception as e:
        print("Some error occured here ==> ", e)

    finally:
        print("Thank you for using my calculator....!")

# Call the function to execute the program:
Height(Given_Height)