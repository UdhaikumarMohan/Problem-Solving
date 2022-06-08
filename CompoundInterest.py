# Write a program to compute compound interest. Hint: (P (1 + r/n)^(nt), where P is the initial principal balance, r is the interest rate, n is the number of times interest is compounded per time period and t is the number of time periods.
# P==> Principal amount, r==> Rate of interest, n==> Rate of interest compounded per time period, t==> Time period.

# Compound interest calculation is quite challenging than calculating simple interest.
# Here we need to clear about the terms.
# P is a principle amount and t is a time period in years, so no problem with it.
# But in the case of rate of interest(r) it should be given in percentage, but we have to calculate it in decimal.
# Which means (r/100).
# Here the term n is very important. If it is yearly means than it is compounded 1 time, Halfyearly means it should be compunded 2 times, Quaterly means than it should be compunded 4 times.
# The important thing is just we have to know how many times it is going to compunded in the given time period.

# Input from user:
P = eval(input("Enter the principal amount in $: "))
r = eval(input("Enter the Rate of the interest in %: "))
n = eval(input("Enter the No. of times compounded per time period: "))
t = eval(input("Enter the time period in years: "))

# Define the function.
def comp_Int(P, r, n, t):

    # We need to deal with errors: Exception handling.
    try:
        # First find total amount after certain years.
        r = r/100
        Total_amount = P*((1+(r/n))**(n*t))

        # No calculate the compound interest by subtracting Principle amount(P) with Total_amount.
        CI = Total_amount - P

        # Output==> 1st way
        print("The Compound Interest for given input is %.3f" %CI)

        # Output==> 2nd way
        result = "The Compound Interest for given amount {0}, rate of interest {1} % of the time period {2} year and number of times compounded per time period {3} is {4} $"
        print(result.format(P, r, t, n, CI))

    except Exception as e:
        print("Some error occurs ==> ", e)

    finally:
        print("Thank you User....!")

# Call the function:
comp_Int(P, r, n, t)





