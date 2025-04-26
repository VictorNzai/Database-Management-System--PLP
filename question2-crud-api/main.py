# main.py

from fastapi import FastAPI, HTTPException
from database import get_connection
from models import User, Task, Comment

app = FastAPI()

# CREATE user
@app.post("/users/")
def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (user.name, user.email, user.password))
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}

# CREATE task
@app.post("/tasks/")
def create_task(task: Task):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (user_id, title, description, status, due_date) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (task.user_id, task.title, task.description, task.status, task.due_date))
    conn.commit()
    conn.close()
    return {"message": "Task created successfully"}

# READ tasks
@app.get("/tasks/")
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# UPDATE task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE tasks
        SET title=%s, description=%s, status=%s, due_date=%s
        WHERE id=%s
    """
    cursor.execute(query, (task.title, task.description, task.status, task.due_date, task_id))
    conn.commit()
    conn.close()
    return {"message": "Task updated successfully"}

# DELETE task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted successfully"}
