# Find Body Mass index of the person using Height and Weight of that person:
# Hint: (Weight/Height x Height)

# Getting User Input:
Weight = eval(input("Enter the Wight of the person in Kilogram: "))
Height = eval(input("Enter th Height of the person in Meter: "))

# Define the Function
def BMI(Weight, Height):

    # Negative values are not allowed.
    try:
        if Weight>=0 and Height>=0:
            X = Weight/pow(Height, 2)
            print("The BMI of the person with given Height and Weight is %.2f" %X)
        else:
            result = "Negative values are not allowed Weight {}, Height {}"
            print (result.format(Weight, Height))
            #print("Negative values are not allowed")

    except Exception as e:
        print("Error Occured ==>", e)

# Call the function to execute the program:
BMI(Weight, Height)