### Below is a menu-driven Python program that performs file operations using pickling and unpickling. It allows you to:

#Add a record

# a record by ID

#Delete a record by ID

##Edit a record by ID

#Display all records

#It stores records in a binary file using the pickle module



import pickle
import os

file_name = "records.dat"

# Function to add record
def add_record():
    f = open(file_name, "ab")
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    
    record = [id, name, age]
    pickle.dump(record, f)
    f.close()
    print("Record added successfully!")

# Function to display all records
def display_records():
    try:
        f = open(file_name, "rb")
        print("\nAll Records:")
        while True:
            record = pickle.load(f)
            print("ID:", record[0], "Name:", record[1], "Age:", record[2])
    except EOFError:
        f.close()

# Function to search record
def search_record():
    sid = int(input("Enter ID to search: "))
    found = False
    
    try:
        f = open(file_name, "rb")
        while True:
            record = pickle.load(f)
            if record[0] == sid:
                print("Record Found:", record)
                found = True
                break
    except EOFError:
        f.close()
    
    if not found:
        print("Record not found!")

# Function to delete record
def delete_record():
    did = int(input("Enter ID to delete: "))
    found = False
    
    f = open(file_name, "rb")
    temp = open("temp.dat", "wb")
    
    try:
        while True:
            record = pickle.load(f)
            if record[0] != did:
                pickle.dump(record, temp)
            else:
                found = True
    except EOFError:
        f.close()
        temp.close()
    
    os.remove(file_name)
    os.rename("temp.dat", file_name)
    
    if found:
        print("Record deleted successfully!")
    else:
        print("Record not found!")

# Function to edit record
def edit_record():
    eid = int(input("Enter ID to edit: "))
    found = False
    
    f = open(file_name, "rb")
    temp = open("temp.dat", "wb")
    
    try:
        while True:
            record = pickle.load(f)
            if record[0] == eid:
                print("Current Record:", record)
                name = input("Enter new Name: ")
                age = int(input("Enter new Age: "))
                record = [eid, name, age]
                found = True
            pickle.dump(record, temp)
    except EOFError:
        f.close()
        temp.close()
    
    os.remove(file_name)
    os.rename("temp.dat", file_name)
    
    if found:
        print("Record updated successfully!")
    else:
        print("Record not found!")

# Menu Driven Program
while True:
    print("\nMENU")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        search_record()
    elif ch == 3:
        delete_record()
    elif ch == 4:
        edit_record()
    elif ch == 5:
        display_records()
    elif ch == 6:
        print("Program Ended")
        break
    else:
        print("Invalid Choice!")