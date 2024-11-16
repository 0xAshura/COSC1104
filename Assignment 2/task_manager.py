import sqlite3
from datetime import datetime

# Database setup
def initialize_database():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT,
            due_date TEXT,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()

# CRUD Operations
def add_task(title, category, due_date=None):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (title, category, due_date) VALUES (?, ?, ?)", (title, category, due_date))
    connection.commit()
    connection.close()

def view_tasks(filter_by=None):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    query = "SELECT id, title, category, due_date, completed FROM tasks"
    if filter_by == "pending":
        query += " WHERE completed = 0"
    elif filter_by == "completed":
        query += " WHERE completed = 1"
    query += " ORDER BY due_date"
    cursor.execute(query)
    tasks = cursor.fetchall()
    connection.close()
    return tasks

def search_tasks(keyword):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, category, due_date, completed FROM tasks WHERE title LIKE ?", (f"%{keyword}%",))
    tasks = cursor.fetchall()
    connection.close()
    return tasks

def mark_task_completed(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

def remove_task(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

def edit_task(task_id, title=None, category=None, due_date=None):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    if title:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
    if category:
        cursor.execute("UPDATE tasks SET category = ? WHERE id = ?", (category, task_id))
    if due_date:
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (due_date, task_id))
    connection.commit()
    connection.close()

# Helper functions
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task[4] else "Pending"
            due_date = task[3] if task[3] else "No due date"
            overdue = False
            if task[3]:
                task_date = datetime.strptime(task[3], "%Y-%m-%d")
                if not task[4] and task_date < datetime.now():
                    overdue = True
            highlight = " (Overdue)" if overdue else ""
            print(f"[{task[0]}] {task[1]} - {task[2]} (Due: {due_date}{highlight}) - {status}")

# Menu-based Interface
def main():
    initialize_database()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Search Tasks")
        print("6. Edit Task")
        print("7. Mark Task as Completed")
        print("8. Remove Task")
        print("9. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            category = input("Enter task category: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
            due_date = due_date if due_date else None
            try:
                if due_date:
                    datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
                add_task(title, category, due_date)
                print("Task added successfully!")
            except ValueError:
                print("Invalid date format. Task not added.")
        elif choice == "2":
            tasks = view_tasks()
            display_tasks(tasks)
        elif choice == "3":
            tasks = view_tasks("pending")
            display_tasks(tasks)
        elif choice == "4":
            tasks = view_tasks("completed")
            display_tasks(tasks)
        elif choice == "5":
            keyword = input("Enter keyword to search: ").strip()
            tasks = search_tasks(keyword)
            display_tasks(tasks)
        elif choice == "6":
            try:
                task_id = int(input("Enter task ID to edit: ").strip())
                title = input("Enter new title (leave blank to keep unchanged): ").strip()
                category = input("Enter new category (leave blank to keep unchanged): ").strip()
                due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep unchanged): ").strip()
                due_date = due_date if due_date else None
                edit_task(task_id, title if title else None, category if category else None, due_date)
                print("Task updated successfully!")
            except ValueError:
                print("Invalid input.")
        elif choice == "7":
            try:
                task_id = int(input("Enter task ID to mark as completed: ").strip())
                mark_task_completed(task_id)
                print("Task marked as completed.")
            except ValueError:
                print("Invalid task ID.")
        elif choice == "8":
            try:
                task_id = int(input("Enter task ID to remove: ").strip())
                remove_task(task_id)
                print("Task removed.")
            except ValueError:
                print("Invalid task ID.")
        elif choice == "9":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
