
# Find the smallest among three numbers.

A = eval(input("Enter the Value of A: "))
B = eval(input("Enter the value of B: "))
C = eval(input("Enter the value of C: "))

class Smallest:

    def __init__(self, A, B, C):

        self.A = A
        self.B = B
        self.C = C

    def Smallest_Condition(self):

        temp = 0

        if self.A < self.B:
            temp = self.A

            if self.C < temp:
                temp = self.C

            else:
                temp = temp
                
        else:
            temp = self.B

            if self.C < temp:
                temp = self.C

            else:
                temp = temp

        return(f"{temp} is the Smallest among the given Numbers")                      

Number = Smallest(A,B,C)

print(Number.Smallest_Condition())