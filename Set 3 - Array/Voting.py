# 6. Read the age of a candidate and determine whether he/she is eligible for casting his/her own vote.

class Vote():

    def __init__(self, *Args):

        self.Name, self.Age = Args

    def Eligibility(self):

        Age = int(self.Age)

        if (Age >= 18): return f"\n The Candiate '{self.Name}' is eligible to cast his/her vote"

        else: return f"\n The Candiate '{self.Name}' is not eligible to cast his/her vote"

    @classmethod
    def Candidate_Entry(cls, Details):

        return cls(*Details.split(','))
        
Candidate = input("\n Enter the candidate name and age in comma seperation: ")
Person = Vote.Candidate_Entry(Candidate)

print(Person.Eligibility())
