import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


# Add new task
def add_task(tasks):
    task = input("Enter your task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty.\n")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("=== TO DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()