import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task.completed else "Pending"
            print(f"{idx}. Title: {task.title}, Description: {task.description}, Category: {task.category}, Status: {status}")

def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category (e.g., Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    print(f"Task '{title}' added successfully!")

def mark_task_completed(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        print(f"Task '{tasks[task_num].title}' marked as completed!")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nPersonal To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
