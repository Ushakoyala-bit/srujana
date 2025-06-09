def task():
    tasks = []  # empty list
    print("----Welcome to the task management app----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are: {tasks}")

    while True:
        try:
            operation = int(input("\nEnter an option:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))
            
            if operation == 1:
                add = input("Enter the task you want to add: ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update: ")
                if updated_val in tasks:
                    up = input("Enter the new task: ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Task '{updated_val}' has been updated to '{up}'.")
                else:
                    print(f"Task '{updated_val}' not found.")

            elif operation == 3:
                delete_val = input("Enter the task name you want to delete: ")
                if delete_val in tasks:
                    tasks.remove(delete_val)
                    print(f"Task '{delete_val}' has been deleted.")
                else:
                    print(f"Task '{delete_val}' not found.")

            elif operation == 4:
                print(f"Current tasks: {tasks}")

            elif operation == 5:
                print("Exiting the task management app. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Call the task function to start the app
task()


