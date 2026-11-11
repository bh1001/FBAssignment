class Student:
    # Parameterized constructor
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Accept method
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Display method
    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("Rank:", self.calculateRank())

    # Method to calculate rank
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

    # Override __str__ method
    def __str__(self):
        return f"StudentID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}"


# Inherited class
class Result(Student):
    def showResult(self):
        print("\nStudent Result Details")
        self.display()


# Creating object
s1 = Result(101, "Rahul", 20, 82)

# Using methods
print(s1)        # Calls __str__
s1.showResult()