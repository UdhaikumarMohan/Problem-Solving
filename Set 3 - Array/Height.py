
# 7. Program to accept the height of a person in centimetres and categorize the person according to their height (tall, short or medium – assume threshold values)

# Lesser than 155cm - Short
# Between 156 - 170 - Medium
# above 170 - Tall

class Height_Calculation:

    Shortest_Person = 54.64
    Tallest_Person = 272
    Threshold_Short = 163
    Threshold_Tall = 177

    def __init__(self, H):
        
        self.H = H
    
    def Height_Method(self):

        if (self.H < 0): print(f"\n The given height {self.H} cm is invalid")

        elif (self.H > 0) and (self.H < Height_Calculation.Shortest_Person): print(f"\n Short, But the given height {self.H} cm is lesser than the height of the shoretest person is {Height_Calculation.Shortest_Person} cm.")
        
        elif (self.H >= Height_Calculation.Shortest_Person) and (self.H <= Height_Calculation.Threshold_Short): print(f"\n Short, Height: {self.H} cm.")
        
        elif (self.H >= Height_Calculation.Threshold_Short) and (self.H < Height_Calculation.Threshold_Tall): print(f"\n Medium, Height: {self.H} cm.")

        elif (self.H >= Height_Calculation.Threshold_Tall) and (self.H <= Height_Calculation.Tallest_Person): print(f"\n Tall, Height: {self.H} cm.")
        
        elif (self.H > Height_Calculation.Tallest_Person): print(f"\n Tall, But the given height {self.H} cm is greater than the height of the shoretest person is {Height_Calculation.Tallest_Person} cm.")

H = eval(input("\n Enter the Height of the person in cm: "))

Person = Height_Calculation(H)

Person.Height_Method()