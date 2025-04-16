task_list = []
while True:
    end_task = input("are you sure you want to end the task (yes/no): ").lower().strip()
    if end_task in {"yes", "no"}:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

print(f"You chose: {end_task}")