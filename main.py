
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Task Manager API")

tasks = [
    {"id": 1, "title": "Complete CI/CD lab", "completed": False},
    {"id": 2, "title": "Study Kubernetes", "completed": False},
]


class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Student Task Manager API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def add_task(task: Task):
    new_task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": task.title,
        "completed": task.completed,
    }
    tasks.append(new_task)
    return new_task


@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise HTTPException(status_code=404, detail="Task not found")
