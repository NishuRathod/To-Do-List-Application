from app.todo_manager import TodoApp

def main():
    todo = TodoApp()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            desc = input("Enter task: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                todo.complete_task(task_id)
            except:
                print("Enter valid number")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
