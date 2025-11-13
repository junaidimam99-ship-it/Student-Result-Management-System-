import json
import os

FILE = "students.json"

# Load existing data
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = []
else:
    data = []

def save_data():
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))

    total = sum(marks)
    grade = "A" if total >= 250 else "B" if total >= 200 else "C"

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "grade": grade
    }

    data.append(student)
    save_data()
    print("Student added successfully!\n")

def view_students():
    if not data:
        print("No records found.\n")
        return

    for s in data:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}, Total: {s['total']}, Grade: {s['grade']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in data:
        if s['roll'] == roll:
            print(f"Record found: {s}\n")
            return
    print("No record found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    global data
    data = [s for s in data if s['roll'] != roll]
    save_data()
    print("Record deleted successfully!\n")

def update_student():
    roll = input("Enter roll number to update: ")
    for s in data:
        if s["roll"] == roll:
            new_marks = list(map(int, input("Enter new marks: ").split()))
            s["marks"] = new_marks
            s["total"] = sum(new_marks)
            s["grade"] = "A" if s["total"] >= 250 else "B" if s["total"] >= 200 else "C"
            save_data()
            print("Record updated!\n")
            return
    print("Record not found.\n")

def menu():
    while True:
        print("----- Student Result Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()
