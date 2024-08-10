import json

tasks = []

def get_input(prompt):
    return input(f"{prompt}: ")

def add_task():
    task = {
        "task": get_input("Enter Task"),
        "deadline": get_input("Enter Deadline (YYYY-MM-DD)"),
        "priority": get_input("Enter Priority (High, Medium, Low)")
    }
    tasks.append(task)
    print(f"Task '{task['task']}' added with deadline {task['deadline']} and priority {task['priority']} is added.")
    save_tasks() 

def display_tasks():
    if not tasks:
        print("No tasks currently.")
    else:
        print("Current Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"#{idx}: {task['task']} | Deadline: {task['deadline']} | Priority: {task['priority']}")

def remove_task():
    display_tasks()
    if tasks:
        task_num = int(get_input("Enter the task number to remove")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Removed: {removed_task['task']}")
            save_tasks()  
        else:
            print("Invalid task number.")

def mark_as_done():
    display_tasks()
    if tasks:
        task_num = int(get_input("Enter the task number to mark as done")) - 1
        if 0 <= task_num < len(tasks):
            done_task = tasks.pop(task_num)
            print(f"Completed: {done_task['task']}")
            save_tasks() 
        else:
            print("Invalid task number.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            global tasks
            tasks = json.load(file)
            print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

def menu():
    return get_input("\nMenu:\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Mark as Done\n5. Exit\nChoose an option")

if __name__ == "__main__":
    load_tasks()
    while True:
        choice = menu()
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            mark_as_done()
        elif choice == "5":
            save_tasks()
            break
        else:
            print("Invalid choice.")
    print("Goodbye!")
