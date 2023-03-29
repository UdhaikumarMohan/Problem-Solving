
# Binary Search problems using OOP.

class Binary_Search:

    def __init__(self, Array):

        self.Array = Array
        self.mid = None

# Write a method to find a Binary Search
    def search(self, N):
        
        min = 0
        max = len(self.Array)-1

        while min <= max:

            mid = (min+max)//2

            if self.Array[mid] == N:
                print(f"\nThe given Number {N} found at index {mid} of the list {self.Array}")
                self.mid = mid
                return True

            elif self.Array[mid] > N: max = mid-1

            elif self.Array[mid] < N: min = mid+1

        print(f"\nThe given Number {N} not found in the list {self.Array}")
        return 
    

    # Write a method to count multiple Numbers in array

    def Count_Num(self, N):

        if self.search(N) == True:

            count = 1

            if self.Array[self.mid-1] == N:

                dec = self.mid-1
                while self.Array[dec] == N:

                    dec-=1
                    count+=1
            else:
                pass
            
            if self.Array[self.mid+1] == N:

                inc = self.mid+1
                while self.Array[inc] == N:

                    inc+=1
                    count+=1
            print(f"\nThe Number {N} occured {count} times in the list {self.Array}")

            return count
        else:
            print(f"\nThe given Number {N} is not found in the list ")
            return -1
        

C = int(input("\nEnter the count of the elements: "))

E = input("\nEnter the elements in comma seperation: ")

Array = list(map(int, E.strip().split(',')))[:C]

N = int(input("\nEnter the Number to search: "))

obj = Binary_Search(Array)

obj.search(N)
obj.Count_Num(N)

