import json

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def view_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

if __name__ == "__main__":
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
