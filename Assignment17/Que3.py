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
class MedicalStudent(Student):
    def __init__(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Internship Marks: "))

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Marks Of Internship:", self.marksOfInternship)
        print("Rank:", self.calculateRank())

    # Override CalculateRank
    def calculateRank(self):
        total = self.percentage + (self.marksOfInternship / 2)
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

    # Override __str__ method
    def __str__(self):
        return f"ID:{self.studentId}, Name:{self.name}, Specialization:{self.specialization}, Percentage:{self.percentage}, InternshipMarks:{self.marksOfInternship}"


# Creating object
m1 = MedicalStudent(201, "Riya", 22, 68, "Cardiology", 40)

print(m1)      # Calls overridden __str__
m1.display()