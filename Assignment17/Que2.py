# Base Class
class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"ID:{self.studentId}, Name:{self.name}, Age:{self.age}, Percentage:{self.percentage}"


# Derived Class
class EnggStudent(Student):
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internalMarks)
        print("Rank:", self.calculateRank())

    # Override CalculateRank
    def calculateRank(self):
        total = self.percentage + (self.internalMarks / 2)
        if total >= 85:
            return "Excellent"
        elif total >= 70:
            return "Very Good"
        elif total >= 55:
            return "Good"
        elif total >= 40:
            return "Average"
        else:
            return "Fail"

    # Override __str__
    def __str__(self):
        return f"ID:{self.studentId}, Name:{self.name}, Branch:{self.branch}, Percentage:{self.percentage}, InternalMarks:{self.internalMarks}"


# Creating object
e1 = EnggStudent(101, "Amit", 20, 72, "Computer", 40)

print(e1)     # Calls overridden __str__
e1.display()