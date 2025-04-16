task_list = []


def show_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")


def add_task():
    description = input("Enter task description: ")
    task_list.append({"description": description, "done": False})
    print(f"Task '{description}' added successfully!")


def view_tasks():
    if not task_list:
        print("No tasks in the list.")
        return

    print("\nCurrent Tasks:")
    for index, task in enumerate(task_list, 1):
        status = "X" if task["done"] else " "
        print(f"{index}. [{status}] {task['description']}")


def remove_task():
    view_tasks()
    if not task_list:
        return

    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num - 1)
            print(f"Task '{removed_task['description']}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_done():
    view_tasks()
    if not task_list:
        return

    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(task_list):
            task_list[task_num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    print("Welcome to Simple Task Manager!")

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

