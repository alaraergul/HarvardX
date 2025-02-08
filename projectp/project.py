import datetime

tasks = []

def main():
    print("Smart Task and Reminder Management System")
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task status")
        print("4. Send reminder")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Task name: ")
            description = input("Description: ")
            due_date_input = input("Due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_input, "%Y-%m-%d")
            add_task(task_name, description, due_date)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Task ID to update: "))
            status = input("New status (completed, pending, cancelled): ")
            update_status(task_id, status)
        elif choice == "4":
            task_id = int(input("Task ID to send reminder for: "))
            send_reminder(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def add_task(task_name, description, due_date):
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "name": task_name,
        "description": description,
        "due_date": due_date,
        "status": "pending"
    }
    tasks.append(task)
    print(f"Task added: {task_name}")

def list_tasks():
    if not tasks:
        print("No tasks.")
        return
    for task in tasks:
        status = task["status"]
        due_in = (task["due_date"] - datetime.datetime.now()).days
        print(f"ID: {task['id']}, Name: {task['name']}, Status: {status}, Due Date: {task['due_date'].date()}, Days Left: {due_in}")

def update_status(task_id, status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            print(f"Task updated: {task['name']}, New status: {status}")
            return
    print("Task not found.")

def send_reminder(task_id):
    for task in tasks:
        if task["id"] == task_id:
            days_left = (task["due_date"].date() - datetime.datetime.now().date()).days
            if days_left > 0:
                print(f"Reminder: '{task['name']}' is due in {days_left} day(s).")
            elif days_left == 0:
                print(f"Reminder: '{task['name']}' is due today!")
            else:
                print(f"Warning: '{task['name']}' is overdue!")
            return
    print("Task not found.")

if __name__ == "__main__":
    main()
