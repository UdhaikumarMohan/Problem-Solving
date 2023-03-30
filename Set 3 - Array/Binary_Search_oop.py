
# Binary Search problems using OOP.


# Getting Input from user.
C = int(input("\n Enter the count of the elements: "))

E = input("\n Enter the elements in comma seperation: ")

Array = list(map(int, E.strip().split(',')))[:C]

N = int(input("\n Enter the Number to search: "))

class Binary_Search:

    def __init__(self, Array):

        self.Array = Array
        # mid is used to store the index of the given number. If the number is not in the list, then the index value will stays as none.
        self.mid = None
        # count is used to store the count of the given number in the list.
        self.count = None
        # Instance variable to store the first occurence index.
        self.First_index = None
        # Instance variable to store the second occurence index
        self.Second_index = None

# Write a method to find a Binary Search
    def search(self, N):
        
        min = 0
        max = len(self.Array)-1

        while min <= max:

            mid = (min+max)//2

            if self.Array[mid] == N:
                self.mid = mid
                return True

            elif self.Array[mid] > N: max = mid-1

            elif self.Array[mid] < N: min = mid+1

        return False
    

# Write a method to count multiple Numbers in array
    def Count_Num(self, N):

        # Execute if only the given number exists in the list. Else just return -1.
        if self.search(N) == True:

            self.count = 1

            if self.Array[self.mid-1] == N:

                dec = self.mid-1
                while (self.Array[dec] == N) and (dec >= 0):

                    dec-=1
                    self.count+=1
            else: pass
            
            if self.Array[self.mid+1] == N:

                inc = self.mid+1
                while(inc < len(self.Array)) and (self.Array[inc] == N):

                    inc+=1
                    self.count+=1
            else: pass

            return self.count
        
        else: return -1

# Write a method to find the first occurence of the Number.

    def Index_Occ(self, N):

        if self.search(N) == True:

            self.First_index = self.mid
            self.Second_index = -1

            if self.Array[self.mid-1] == N:

                dec = self.mid-1
                while (dec >= 0) and (self.Array[dec] == N):

                    self.First_index = dec
                    self.Second_index = dec+1
                    dec-=1

            elif self.Array[self.mid+1] == N: self.Second_index = self.mid+1

            dict = {"First_index":self.First_index, "Second_index":self.Second_index}

            return (dict)
        
        else:
            dict = {"First_index":-1, "Second_index":-1}
            return(dict)

def main():

# Declare object:
    obj = Binary_Search(Array)

# Search the given number is exists or not: Call search method
    if obj.search(N) == True: print(f"\n The given Number {N} found at index {obj.mid} of the list {obj.Array}")

    else: print(f"\nThe given Number {N} not found in the list {obj.Array}")

# Count of the given element in the list: Call Count_Num method
    if obj.Count_Num(N) >=1: print(f"\n The given Number {N} occurs {obj.count} times in the list {obj.Array} ")

    else: pass

# Find index of the first occurence

    if obj.Index_Occ(N)["First_index"] >= 0: print(f"\n The First occurence of the given Number {N} is found at index {obj.First_index} from the list {obj.Array}")

    else: pass

# Find index of the second 

    if obj.Index_Occ(N)["Second_index"] >= 1: print(f"\n The Second occurence of the given Number {N} is found at index {obj.Second_index} from the list {obj.Array}")

    else: print(f"\n The given Number {N} occured only once in the list {obj.Array}")

if __name__ == '__main__': main()

