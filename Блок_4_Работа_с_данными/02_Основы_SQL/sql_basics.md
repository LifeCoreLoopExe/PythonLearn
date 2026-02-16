# 🗄️ Основы SQL

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Освоить основные SQL команды для работы с базами данных.

---

## 📚 Основные команды

### CREATE TABLE - создание таблицы

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### INSERT - вставка данных

```sql
INSERT INTO users (username, email, age)
VALUES ('alice', 'alice@example.com', 25);

INSERT INTO users (username, email, age)
VALUES 
    ('bob', 'bob@example.com', 30),
    ('charlie', 'charlie@example.com', 28);
```

### SELECT - выборка данных

```sql
-- Все столбцы
SELECT * FROM users;

-- Конкретные столбцы
SELECT username, email FROM users;

-- С условием
SELECT * FROM users WHERE age > 25;

-- Сортировка
SELECT * FROM users ORDER BY age DESC;

-- Ограничение количества
SELECT * FROM users LIMIT 10;
```

### UPDATE - обновление данных

```sql
UPDATE users
SET age = 26
WHERE username = 'alice';
```

### DELETE - удаление данных

```sql
DELETE FROM users
WHERE id = 1;
```

### WHERE - фильтрация

```sql
-- Сравнение
SELECT * FROM users WHERE age >= 25;

-- AND, OR
SELECT * FROM users WHERE age > 20 AND age < 30;

-- IN
SELECT * FROM users WHERE username IN ('alice', 'bob');

-- LIKE (поиск по шаблону)
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- BETWEEN
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
```

### JOIN - объединение таблиц

```sql
-- Есть две таблицы: users и orders

-- INNER JOIN
SELECT users.username, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN
SELECT users.username, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

### GROUP BY - группировка

```sql
-- Количество пользователей по возрасту
SELECT age, COUNT(*) as count
FROM users
GROUP BY age;

-- С условием на группы
SELECT age, COUNT(*) as count
FROM users
GROUP BY age
HAVING count > 1;
```

---

## 💻 Практические примеры с Python

### Пример: SQLite в Python

```python
import sqlite3

# Подключение к БД
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

# Вставка данных
cursor.execute('''
    INSERT INTO users (username, email, age)
    VALUES (?, ?, ?)
''', ('alice', 'alice@example.com', 25))

# Выборка данных
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()
```

---

## 📖 Ресурсы для изучения

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python Docs - sqlite3](https://docs.python.org/3/library/sqlite3.html)

---

[← Вернуться к roadmap](README.md)
