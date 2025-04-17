task_list = []
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    option = 0
    option = int(input ("Enter your option (1-5): "))
    if option == 1:
        task = input("Enter your Task : ")
        task_list.append(task)
        print("Task added successfully")
    elif option == 2:
        for task in task_list:
            print("Tasks:", task)
    elif option == 3:
        for task in task_list:
            print("Tasks:", task)
        task = input("Enter the task you want to remove: ")
        task_list.remove(task)
        print("Task removed successfully")
    elif option == 4:
        for task in range(len(task_list)):
            if task_list[task] == task:
                task_list[task] = "Done"
        if not task_list:
            print("No tasks to mark as done")
    elif option == 5:
        print("Exiting Task Manager")
        break