
# Find the largest among three numbers.

A = eval(input("Enter the Value of A: "))
B = eval(input("Enter the value of B: "))
C = eval(input("Enter the value of C: "))

class Largest:
    
    def __init__(self, A, B, C):

        self.A = A
        self.B = B
        self.C = C

    def Largest_Condition(self):

        temp = 0

        if self.A > self.B:
            temp = self.A

            if self.C > temp:
                temp = self.C

            else:
                temp = temp
                
        else:
            temp = self.B

            if self.C > temp:
                temp = self.C

            else:
                temp = temp

        return(f"{temp} is the Largest among the given Numbers")                      

Number = Largest(A,B,C)

print(Number.Largest_Condition())