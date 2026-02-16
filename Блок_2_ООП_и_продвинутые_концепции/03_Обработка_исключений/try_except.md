# ⚠️ Try, Except, Finally

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Научиться обрабатывать ошибки и исключения для создания надёжных программ.

---

## 📚 Теория

### Базовый синтаксис

```python
try:
    # Код, который может вызвать ошибку
    result = 10 / 0
except ZeroDivisionError:
    # Обработка конкретной ошибки
    print("Ошибка: деление на ноль!")
```

### Множественные except

```python
try:
    number = int(input("Введите число: "))
    result = 10 / number
except ValueError:
    print("❌ Это не число!")
except ZeroDivisionError:
    print("❌ Деление на ноль!")
except Exception as e:
    print(f"❌ Неожиданная ошибка: {e}")
```

### Finally блок

```python
try:
    file = open('file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("❌ Файл не найден")
finally:
    # Выполнится в любом случае
    print("Очистка ресурсов...")
    if 'file' in locals():
        file.close()
```

### Else блок

```python
try:
    number = int(input("Введите число: "))
except ValueError:
    print("❌ Неверный ввод")
else:
    # Выполнится, если НЕ было ошибок
    print(f"✅ Вы ввели: {number}")
```

### Создание собственных исключений

```python
class InsufficientFundsError(Exception):
    """Исключение для недостатка средств"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счёте")
        self.balance -= amount

# Использование
try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"❌ {e}")
```

---

## 💻 Практические примеры

### Пример 1: Безопасный ввод числа

```python
def safe_input_int(prompt):
    """Безопасный ввод целого числа"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Пожалуйста, введите целое число")

age = safe_input_int("Введите возраст: ")
print(f"Вам {age} лет")
```

### Пример 2: Чтение файла с обработкой ошибок

```python
def read_file_safe(filename):
    """Безопасное чтение файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден")
        return None
    except PermissionError:
        print(f"❌ Нет прав доступа к файлу {filename}")
        return None
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return None

content = read_file_safe('data.txt')
if content:
    print(content)
```

---

## ✅ Задачи для практики

### Задача 1: Калькулятор с обработкой ошибок
Создайте калькулятор, который обрабатывает:
- Неверный ввод (не число)
- Деление на ноль
- Неизвестную операцию

### Задача 2: Конвертер файлов
Создайте программу конвертации текстовых файлов с обработкой:
- Файл не найден
- Проблемы с кодировкой
- Недостаточно места на диске

---

## 📖 Ресурсы для изучения

- [Python Docs - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python - Python Exceptions](https://realpython.com/python-exceptions/)

---

[← Вернуться к roadmap](README.md)
