# 🌐 Web-разработка с Flask/FastAPI

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Освоить основы веб-разработки на Python с использованием Flask или FastAPI.

---

## 📚 Flask - Основы

### Установка

```bash
pip install flask
```

### Простое приложение

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return "Привет, Flask!"

# API endpoint
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Алиса"},
        {"id": 2, "name": "Боб"}
    ]
    return jsonify(users)

# POST запрос
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "Пользователь создан", "data": data}), 201

# Динамический route
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    return jsonify({"id": user_id, "name": "Пользователь"})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🚀 FastAPI - Основы

### Установка

```bash
pip install fastapi uvicorn
```

### Простое приложение

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Модель данных
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory база данных
users = []

@app.get("/")
def read_root():
    return {"message": "Привет, FastAPI!"}

@app.get("/api/users")
def get_users():
    return users

@app.post("/api/users")
def create_user(user: User):
    users.append(user)
    return {"message": "Пользователь создан", "user": user}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

# Запуск: uvicorn main:app --reload
```

---

## 💻 Практический пример: TODO API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="TODO API")

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# База данных (в реальности используйте SQL/NoSQL)
tasks_db = []
task_id_counter = 1

@app.get("/")
def root():
    return {"message": "TODO API", "docs": "/docs"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """Получить все задачи"""
    return tasks_db

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    """Создать новую задачу"""
    global task_id_counter
    task.id = task_id_counter
    task_id_counter += 1
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Получить задачу по ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    """Обновить задачу"""
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task.id = task_id
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Удалить задачу"""
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")

# Запуск: uvicorn main:app --reload
# Документация: http://127.0.0.1:8000/docs
```

---

## 📖 Ресурсы для изучения

- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Real Python - Flask Tutorial](https://realpython.com/tutorials/flask/)

---

[← Вернуться к roadmap](README.md)
