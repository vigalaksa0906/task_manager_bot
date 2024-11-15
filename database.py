import sqlite3

DB_NAME = 'tasks.db'

def create_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    """Create the 'tasks' table if it doesn't exist"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        is_complete BOOLEAN NOT NULL CHECK (is_complete IN (0, 1))
    )
    """)
    conn.commit()
    conn.close()

def add_task(description):
    """Add a new task to the database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, is_complete) VALUES (?, ?)", (description, False))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Delete a task by its ID"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def show_tasks():
    """Retrieve and display all tasks from the database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    """Mark a task as completed"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET is_complete = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
