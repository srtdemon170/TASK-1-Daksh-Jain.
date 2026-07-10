import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add task
def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "id": len(tasks) + 1,
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✓ Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== TASK LIST =====")

    for task in tasks:
        status = "✓ Completed" if task["completed"] else "✗ Pending"

        print(
            f'ID: {task["id"]} | '
            f'Task: {task["task"]} | '
            f'Status: {status}'
        )


# Mark task completed
def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter Task ID to mark completed: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print("✓ Task marked as completed!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Invalid input.")


# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter Task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)

                # Reassign IDs
                for index, task in enumerate(tasks, start=1):
                    task["id"] = index

                save_tasks(tasks)

                print("✓ Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Invalid input.")


# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n==============================")
        print("      TO-DO LIST MANAGER")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nSaving data...")
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()