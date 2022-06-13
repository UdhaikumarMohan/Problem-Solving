# Convert celcisus to Fahrenheit: Hint(F = (C*(9/5))+32).
# Here we are dealing with tempreature so negative values are allowed.
# To counter type error we use exception handling.

# User input:
Celcius = eval(input("Enter the tempreature in °C: "))

# Define the function:
def Tempreature(Celcius):

# Exception handling to counter string values:
    try:
        print("Welcome to Celcius to Fahrenheit converter....")
        Fahrenheit = ((Celcius*(9/5))+32)

        # Formatting ouput (1st way)
        result = "{0} °C is equal to {1} °F "
        print(result.format(Celcius, Fahrenheit))

        # Formatting ouput (2nd way)
        print(str(Celcius) + " °C is equal to %.4f °F" %Fahrenheit)

    except Exception as e:
        print("Invalid input, strings are not allowed -->", e)

    finally:
        print("Thank you for using tempreature converter....")

# Call the function:
Tempreature(Celcius)