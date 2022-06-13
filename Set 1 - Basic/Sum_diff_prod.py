# Given two intergers: Sum, difference and product:

#Define the function and get input through it: 
#(Arithmatic Operation = Arith_Opr.)
def Arith_Opr(Int_1, Int_2):

# Sum of two numbers:
    Sum = Int_1 + Int_2
    print("The sum of Integer_1 and Integer_2 will be: ", Sum)

#Difference between two Integers:
    Difference = (Int_1 - Int_2)
    print("The Difference between two Integers: ", Difference)

#Product between two Integers:
    Product = Int_1 * Int_2
    print("The Product of two Integers are: ", Product)

#Getting Input form user:    
Int_1 = int(input("Enter the Integer_1: "))
Int_2 = int(input("Enter the Integer_2: "))

#Calling the Fuction:
Arith_Opr(Int_1, Int_2)
