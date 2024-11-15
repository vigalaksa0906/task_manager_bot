import unittest
import sqlite3
from database import add_task, delete_task, show_tasks, complete_task, create_table

class TestTaskManagement(unittest.TestCase):

    def setUp(self):
        """Prepare an empty database for testing"""
        # Create a new database and table for each test run
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS tasks")
        create_table()  # Ensure the 'tasks' table is created
        conn.commit()
        conn.close()

    def test_add_task(self):
        """Test adding a task"""
        add_task("Test task 1")
        tasks = show_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test task 1")
        self.assertEqual(tasks[0][2], 0)  # 'is_complete' should be 0 (not completed)

    def test_delete_task(self):
        """Test deleting a task"""
        add_task("Task to delete")
        tasks = show_tasks()
        task_id = tasks[0][0]
        delete_task(task_id)
        tasks = show_tasks()
        self.assertEqual(len(tasks), 0)

    def test_complete_task(self):
        """Test marking a task as completed"""
        add_task("Task to complete")
        tasks = show_tasks()
        task_id = tasks[0][0]
        complete_task(task_id)
        tasks = show_tasks()
        self.assertEqual(tasks[0][2], 1)  # 'is_complete' should be 1 (completed)

    def test_show_tasks(self):
        """Test displaying all tasks"""
        add_task("Task 1")
        add_task("Task 2")
        tasks = show_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Task 1")
        self.assertEqual(tasks[1][1], "Task 2")

if __name__ == '__main__':
    unittest.main()
