# SY/symarks.py

class SYMARKS:
    def __init__(self):
        self.ComputerTotal = 0
        self.MathsTotal = 0
        self.ElectronicsTotal = 0

    def get_marks(self):
        self.ComputerTotal = int(input("Enter Computer Marks: "))
        self.MathsTotal = int(input("Enter Maths Marks: "))
        self.ElectronicsTotal = int(input("Enter Electronics Marks: "))

    def display(self):
        print("\nSY Marks")
        print("Computer:", self.ComputerTotal)
        print("Maths:", self.MathsTotal)
        print("Electronics:", self.ElectronicsTotal)