# Find the area of field in acers whose lengeth and widh are given in field. (Hint: 1 acre = 43,560 sq ft.)
# By taking the product of given length and width, the area of the field is calulated in Square feet.
# To convert it in acers, the otained value shoud be divided by 43,560.

# Get Input from user:
Length = eval(input("Enter the length of the field in feet: "))
Width = eval(input("Enter the width of the field in feet: "))

# Define the fuction:
def Field(Length, Width):
    one_Acer = 43560
    print("Welcome to Area calculator")

# Exception handling: Here we are getting input form user, because of that sometimes input should be given as strings.
# That may leads to the value error. So we use exception handling.
    try:
        Area_in_Sqft = Length * Width
        Area_in_Acer = (Area_in_Sqft/one_Acer)
        Result ="The area of field with the length  {0} ft and width {1} ft is %.3f Acers"
        print(Result.format(Length, Width) %Area_in_Acer)

    except Exception as e:
        print("Some error occured in the execution --> ", e)

    finally:
        print("Thank you for using Area calculator.....")

# Call the fuction to execute the program:
Field(Length, Width)