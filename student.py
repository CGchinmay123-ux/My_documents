import os

# File to store student data
FILE_NAME = "students.txt"

# Load data from file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    return [line.strip().split(",") for line in lines]

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        for record in data:
            file.write(",".join(record) + "\n")

# Add a new student
def add_student(data):
    name = input("Enter student name: ")
    grades = input("Enter grades (comma-separated): ")
    data.append([name, grades])
    save_data(data)
    print("Student added successfully!")

# View all students
def view_students(data):
    print("\n--- Student Records ---")
    for record in data:
        name, grades = record
        print(f"Name: {name}, Grades: {grades}")
    print("-----------------------\n")

# Search for a student
def search_student(data):
    name = input("Enter student name to search: ")
    for record in data:
        if record[0].lower() == name.lower():
            print(f"Found: Name: {record[0]}, Grades: {record[1]}")
            return
    print("Student not found!")

# Update student grades
def update_grades(data):
    name = input("Enter student name to update grades: ")
    for record in data:
        if record[0].lower() == name.lower():
            new_grades = input("Enter new grades (comma-separated): ")
            record[1] = new_grades
            save_data(data)
            print("Grades updated successfully!")
            return
    print("Student not found!")

# Main function
def main():
    data = load_data()
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Grades")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_grades(data)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
