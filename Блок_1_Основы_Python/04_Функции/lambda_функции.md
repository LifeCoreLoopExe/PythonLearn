# λ Lambda-функции

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Освоить использование lambda-функций для создания анонимных функций.

---

## 📚 Теория

### Синтаксис

```python
# Обычная функция
def add(x, y):
    return x + y

# Lambda-функция
add = lambda x, y: x + y

result = add(5, 3)
print(result)  # 8
```

### Использование с встроенными функциями

```python
# map - применить функцию к каждому элементу
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter - отфильтровать элементы
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]

# sorted - сортировка с ключом
students = [
    {"name": "Алиса", "grade": 85},
    {"name": "Боб", "grade": 92},
    {"name": "Чарли", "grade": 78}
]

sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")
```

---

## 💻 Практические примеры

### Пример 1: Сортировка кортежей

```python
points = [(1, 5), (3, 2), (2, 8), (4, 1)]

# Сортировка по второму элементу
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # [(4, 1), (3, 2), (1, 5), (2, 8)]
```

### Пример 2: Обработка строк

```python
words = ["Python", "java", "JAVASCRIPT", "c++", "Ruby"]

# Сортировка без учёта регистра
sorted_words = sorted(words, key=lambda x: x.lower())
print(sorted_words)  # ['c++', 'java', 'JAVASCRIPT', 'Python', 'Ruby']
```

---

## ⚠️ Когда НЕ использовать lambda

```python
# ❌ Сложная логика
process = lambda x: x * 2 if x > 0 else x * -1 if x < 0 else 0

# ✅ Лучше обычная функция
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x * -1
    else:
        return 0
```

---

[← Вернуться к roadmap](README.md)
