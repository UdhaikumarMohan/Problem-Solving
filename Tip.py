# Write the program to calculate the tip to be provided to the waiter, at 5% of bill amount.
# Since we are dealing with Money, Negative values are not allowed.
# User Input:
Bill_Amount = eval(input("Enter the total bill amount in Rupees: "))

# Define the function:
def Tip(Bill_Amount):

# Exception Handling to deal with string inputs.
    try:
        if Bill_Amount >= 0:
            Tip_Amount = (Bill_Amount*(5/100))
            result =  "%.2f $, Provided as a tip for waiter's service form the total bill amount {0} $" %Tip_Amount
            print(result.format(Bill_Amount))

        else:
            print("Amount should not be in Negative numbers, Invalid input")

    except Exception as e:
        print("Some error occured --> ", e)

    finally:
        print("Thank you.....!")

# Call the function to execute the program.
Tip(Bill_Amount)


