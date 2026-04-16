tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
        except:
            print("Error input.")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")