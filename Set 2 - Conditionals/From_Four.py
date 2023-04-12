
# Find the laregest among the four numbers.

A = eval(input("\nEnter the Value of A: "))
B = eval(input("\nEnter the value of B: "))
C = eval(input("\nEnter the value of C: "))
D = eval(input("\nEnter the value of D: "))


class Four_Numbers:

    def __init__(self, A, B, C, D):

        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def Largest_Method(self):

        List = [self.A, self.B, self.C, self.D]

        return(f"\n{max(List)} is the biggest among the four numbers")

Number = Four_Numbers(A,B,C,D)

print(Number.Largest_Method())
