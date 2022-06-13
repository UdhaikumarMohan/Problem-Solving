# Given the basic pay, DA% and TA%, PF @ 8% deduction, calculate the gross pay. Hint: (BasicPay + DA + TA – PF)

# User Input:
Basic = eval(input("Enter the Basic Salary in Rupees: "))
DA = eval(input("Enter the DA in %: "))
TA = eval(input("Enter the TA in %: "))

# Define the function:
def Sal(Basic, DA, TA):

    # The Fixed value of PF is 8%
    # Exception handling to counter the error.
    try:
        PF = ((Basic/100)*8)
        DA = ((Basic/100)*DA)
        TA = ((Basic/100)*TA)
        Gross = (Basic + DA + TA - PF)

        # Formatting output (1st Way)
        result = "{0} is a Net salary of the employe"
        print(result.format(Gross))

        # Formatting output (2nd Way)
        print("%.2f is a Net salary of the employe" %Gross )

    except Exception as e:
        print("Some error occured=> ", e)

    finally:
        print("Thank you for using salary calculator.")

# Call the function to execute the program.
Sal(Basic, DA, TA)