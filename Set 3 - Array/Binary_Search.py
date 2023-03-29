
#Binary Search in the sorted Array.

# Getting input from the user.

C = int(input("Enter the count of the elements: "))

E = input("Enter the elements using comma seperation: ")

Array = list(map(int, E.strip().split(',')))[:C]

N = int(input("Enter the number to search: "))

def Binary_Search_1(N, Array):

    min = 0
    max = len(Array)-1

    while min <= max:

        mid = (min+max)//2

        if Array[mid] == N: return f"The Number {N} found at index {mid}"

        elif Array[mid] < N: min = mid+1

        elif Array[mid] > N: max = mid-1

    return f"The given Number {N} is not found in the list."

print(Binary_Search_1(N, Array))







