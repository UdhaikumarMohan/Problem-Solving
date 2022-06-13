# Generate Random number (1 - 100):

import random

# Define the function
def Rand():
    Random_Number_1 = random.randrange(1, 100)
    Random_Number_2 = random.randint(1, 100)
   
    print(Random_Number_1, Random_Number_2)

# Call the function:
Rand()