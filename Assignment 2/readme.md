# Task Manager  
**Date**: 11/15/2024  
**Author**: Mihir Limbad (100938484)  

## **Description**  
This Python script is a console-based **Task Manager** application designed to help users manage their tasks effectively. The application provides features to add, view, search, edit, and remove tasks. It also allows users to mark tasks as completed and view overdue tasks. All task information is stored persistently using an SQLite database.

---

## **How It Works**  
1. When the script is executed, an SQLite database (`tasks.db`) is initialized to store task details.  
2. The user interacts with a menu-based interface to:  
   - Add tasks with optional categories and due dates.  
   - View all tasks, pending tasks, or completed tasks.  
   - Search for tasks using keywords.  
   - Edit task details such as title, category, or due date.  
   - Mark tasks as completed.  
   - Remove tasks by their ID.  
3. Tasks are displayed with clear information, including due dates and status (Pending, Completed). Overdue tasks are highlighted.  
4. The application validates input (e.g., date format) and handles errors gracefully.

---

## **Usage**  
To run this script:  

1. Ensure you have Python installed on your system.  
2. Save the script in a file named `task_manager.py`.  
3. Open your terminal or command prompt and navigate to the script's directory.  
4. Run the script by executing:  
   ```bash
   python3 task_manager.py
   ```  
5. Use the menu options to manage your tasks.  

---

## **Sample Output**  
```plaintext
Task Manager  
1. Add Task  
2. View All Tasks  
3. View Pending Tasks  
4. View Completed Tasks  
5. Search Tasks  
6. Edit Task  
7. Mark Task as Completed  
8. Remove Task  
9. Exit  
Choose an option: 1  

Enter task title: Complete Project Report  
Enter task category: Work  
Enter due date (YYYY-MM-DD) or leave blank: 2024-11-20  
Task added successfully!  

Task Manager  
1. Add Task  
2. View All Tasks  
Choose an option: 2  

[1] Complete Project Report - Work (Due: 2024-11-20) - Pending
```

---

## **Features**  
- **Add Tasks**: Create new tasks with optional categories and due dates.  
- **View Tasks**: Display all tasks, pending tasks, or completed tasks.  
- **Search**: Find tasks by a keyword in their title.  
- **Edit Tasks**: Update task details like title, category, or due date.  
- **Mark Completed**: Mark a task as completed.  
- **Remove Tasks**: Delete tasks by ID.  
- **Overdue Highlight**: Clearly highlight overdue tasks.  

---

## **Requirements**  
- Python 3.12.0  
- SQLite (pre-installed with Python)  

---

## **Benefits**  
- Simple and intuitive interface for task management.  
- Persistent storage using SQLite.  
- Flexibility to manage tasks across multiple sessions.  
- Organized display of tasks with status and due date information.  
