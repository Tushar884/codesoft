tasks = []

def add_task(task):
    tasks.append(task)  
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(task_index):
    if 1 <= task_index <= len(tasks):  
        removed_task = tasks.pop(task_index - 1)  
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")


while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View taks")
    print("3. Remove a tesk")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)  
    elif choice == '2':
        view_tasks()  
    elif choice == '3':
        view_tasks()  
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)  
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
