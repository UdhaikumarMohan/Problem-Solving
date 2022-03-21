# Convert kilometer into mile: Hint(1km = 0.621371 Mile)

# User Input:

Kilometer = eval(input("Enter the value in km: "))

# Define the function:
def km_conversion(Kilometer):

# Exception handling to counter string values:\
    try:
        print("Welcome user....")

# Conditions to eleminate negative values:
        if (Kilometer>=0):
            Miles = Kilometer * 0.621371
            print(str(Kilometer)+ " km is equal to " + str(Miles)+ " Miles")

        else:
            print("Negative integers not allowed, please give valid integer.")

    except Exception as e:
        print("Invalid input, only integer and decimals are allowed --> ", e)
    
    finally:
        print("Thank you user....")

# Call the function:
km_conversion(Kilometer)
