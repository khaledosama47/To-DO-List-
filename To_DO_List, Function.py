#task:2
#خالد أسامه عبدالعزيز خليفه
#سكشن الاحد

def add_task(tasks):
    task = input("Enter the task you want to add: ").lower().strip()
    if task:
        tasks.append(task)  
        print("Task added successfully!")
    else:
        print("You cannot add an empty task.")

def view_tasks(tasks):
    if tasks:
        print("\nYour TODO List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")  
    else:
        print("\nYour TODO List is empty.")

def delete_task(tasks):
    if tasks:
        task_to_delete = input("Enter the task you want to delete: ").lower().strip()
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)  
            print("Task deleted successfully!")
        else:
            print("Task not found.")
    else:
        print("No tasks available to delete.")

def search_task(tasks):
    search_query = input("Enter the task you want to search for: ").strip()
    matching_tasks = [task for task in tasks if search_query.lower() in task.lower()]
    if matching_tasks:
        print("\nMatching tasks:")
        for task in matching_tasks:
            print(f"- {task}")
    else:
        print("No matching tasks found.")

def todo_list():
    tasks = []
    while True:
        print("\nTODO LIST APP")
        print("1- Add a task")
        print("2- View all tasks")
        print("3- Delete a task")
        print("4- Search for a task")
        print("5- Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            search_task(tasks)
        elif choice == "5":
            print("Thanks for using the TODO list app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

todo_list()
