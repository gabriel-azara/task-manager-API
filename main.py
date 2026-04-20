from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)

tasks: List[Task] = []
current_id = 1

@app.get("/")
def home():
    return {"message": "Rodando API de tarefas!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: TaskCreate):
    global current_id
    
    new_task = Task(
        id=current_id,
        title=task.title,
        done=False
    )
    
    tasks.append(new_task)
    current_id += 1
    
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Tarefa deletada"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")