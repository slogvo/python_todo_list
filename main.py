# File: main.py
import sys
from src.task_manager import TaskManager
from src.storage import Storage


def main():
    storage = Storage("data/tasks.json")
    manager = TaskManager(storage)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice: str = input("Enter choice (1-4): ")

        try:
            if choice == "1":
                name = input("Enter task name: ")
                manager.add_task(name)
                print("Task added!")
            elif choice == "2":
                index = int(input("Enter task index to remove: "))
                manager.remove_task(index)
                print("Task removed!")
            elif choice == "3":
                manager.show_tasks()
            elif choice == "4":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
