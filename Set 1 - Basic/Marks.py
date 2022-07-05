# Program to read Name, Roll No., Mark of threes subjects and find its average.

# Getting Inuput from the user:
Name = eval(input("Enter the Name of the Student: "))
Roll_No = eval(input("Enter the Roll number of the student: "))
N = int(input("Enter the number of the subjects: "))
Mark_List = []

for a in range(1, N+1):
    Elements = float(input("Enter the mark of the subject-" + str(a) + ": "))
    Mark_List.append(Elements)

print(Mark_List)

def Average(Name, Roll_No, N, Mark_List):

    Avg = ((sum(Mark_List))/N)

    print("Name of the Student==> ", Name)
    print("Roll_Number==>", Roll_No)
    print("The Average mark scored by "+ str(Name) + " is " + str(Avg) + " in " + str(N) + " Subjects")

Average(Name, Roll_No, N, Mark_List)

