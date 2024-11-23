import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    print("\n--- Task List ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
        print("-----------------------")
    print()

# Update task status
def update_task(tasks):
    title = input("Enter the task title to update: ")
    for task in tasks:
        if task["title"].lower() == title.lower():
            new_status = input("Enter new status (Pending/Completed): ").capitalize()
            if new_status in ["Pending", "Completed"]:
                task["status"] = new_status
                save_tasks(tasks)
                print("Task status updated successfully!")
                return
            else:
                print("Invalid status. Task not updated.")
                return
    print("Task not found!")

# Delete a task
def delete_task(tasks):
    title = input("Enter the task title to delete: ")
    for task in tasks:
        if task["title"].lower() == title.lower():
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found!")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Tracker Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
