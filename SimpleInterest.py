# Write the program to calculate simple interest. (P*n*r/100)
# P => Principle
# n => No. of years
# r => Rate of Interest

# User Input:
P = eval(input("Enter the principle amount: "))
n = eval(input("Enter the time period in years: "))
r = eval(input("Rate of interest in %: "))

# Define the Function
def Simple_Interest(P, n, r):
    
    # Exceptin Handling to counter input errors:
    try:
        SI = (P*n*(r/100))
        return(SI)

    except Exception as e:
        print("Some error occur at this point ==>", e)

    finally:
        print("Thank you for using my Calculator...!")

# Call the function:
x = Simple_Interest(P, n, r)

# Output==> 1st way
print("The Simple Interest for given input is %.3f" %x)

# Output==> 2nd way

result = "The Simple Interest for given amount {0}, rate of interest {1} % of the time period {2} years is {3} $"
print(result.format(P, r, n, x))
