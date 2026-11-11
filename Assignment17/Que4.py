# Student Class
class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"ID:{self.studentId}, Name:{self.name}, Age:{self.age}, Percentage:{self.percentage}"


# College Class
class College:
    # Parameterized constructor for number of students
    def __init__(self, n):
        self.students = []
        self.max_students = n

    # Add Student
    def AddStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("Cannot add more students.")

    # Get Student
    def GetStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                return s
        return "Student not found"

    # Remove Student
    def RemoveStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                self.students.remove(s)
                print("Student removed successfully.")
                return
        print("Student not found")

    # Override __str__ method
    def __str__(self):
        result = "College Students List:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result


# Example Usage
c1 = College(3)

s1 = Student(101, "Rahul", 20, 75)
s2 = Student(102, "Amit", 21, 68)
s3 = Student(103, "Sneha", 19, 82)

c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)

print(c1)

print("Get Student:", c1.GetStudent(102))

c1.RemoveStudent(101)

print("\nAfter Removing:")
print(c1)