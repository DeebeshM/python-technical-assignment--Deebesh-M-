import json
import os

FILENAME = "students.json"
students = []

# ---------------- JSON SAVE/LOAD ----------------
def load_data():
    global students
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            students = []  # if file is empty or corrupted

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)

# ---------------- FUNCTIONS ----------------
def add_student():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        students.append({"name": name, "age": age, "marks": marks})
        save_data()
        print("✅ Student added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Age/marks must be numbers.\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    print("\n--- All Students ---")
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        for s in found:
            print(f"✅ Found: Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
    else:
        print("❌ Student not found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_data()
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")

# ---------------- MAIN MENU ----------------
def main():
    load_data()  # load existing records at start
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program... Data saved.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
import json
import os

FILENAME = "students.json"
students = []

# ---------------- JSON SAVE/LOAD ----------------
def load_data():
    global students
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            students = []  # if file is empty or corrupted

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)

# ---------------- FUNCTIONS ----------------
def add_student():
    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        students.append({"name": name, "age": age, "marks": marks})
        save_data()
        print("✅ Student added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Age/marks must be numbers.\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    print("\n--- All Students ---")
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        for s in found:
            print(f"✅ Found: Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}")
    else:
        print("❌ Student not found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_data()
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")

# ---------------- MAIN MENU ----------------
def main():
    load_data()  # load existing records at start
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program... Data saved.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
