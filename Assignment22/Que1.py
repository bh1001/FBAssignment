#Here is a simple Python program that creates a class Emp (eid, ename, basic) and stores #objects in a file using pickling and unpickling.

import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def show(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.ename)
        print("Basic Salary:", self.basic)
        print("----------------------")


# Function to add employee
def add_emp():
    f = open("emp.dat", "ab")
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    e = Emp(eid, ename, basic)
    pickle.dump(e, f)
    f.close()
    print("Employee record added successfully")


# Function to display employees
def display_emp():
    try:
        f = open("emp.dat", "rb")
        while True:
            e = pickle.load(f)
            e.show()
    except EOFError:
        f.close()


# Menu
while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_emp()
    elif ch == 2:
        display_emp()
    elif ch == 3:
        break
    else:
        print("Invalid choice")
        
        
#How This Works
#Class Emp → stores employee details (eid, ename, basic)
#Pickling (pickle.dump) → saves object into file emp.dat
#Unpickling (pickle.load) → reads object from file
#File modes used:
#"ab" → append binary
#"rb" → read binary