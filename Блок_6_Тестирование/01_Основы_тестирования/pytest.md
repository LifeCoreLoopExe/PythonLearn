# ✅ Тестирование с pytest

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Научиться писать автоматические тесты для проверки корректности кода.

---

## 📚 Теория

### Установка pytest

```bash
pip install pytest
```

### Базовый тест

```python
# test_calculator.py

def add(a, b):
    return a + b

def test_add():
    """Тест функции сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Запуск: pytest test_calculator.py
```

### Структура теста

```python
# Arrange (Подготовка)
# Act (Действие)
# Assert (Проверка)

def test_division():
    # Arrange
    a = 10
    b = 2
    
    # Act
    result = a / b
    
    # Assert
    assert result == 5
```

### Тестирование исключений

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

### Фикстуры

```python
import pytest

@pytest.fixture
def sample_list():
    """Фикстура для тестовых данных"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_length(sample_list):
    assert len(sample_list) == 5
```

---

## 💻 Практические примеры

### Пример 1: Тестирование класса

```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b

# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(10, 15) == -5

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
```

### Пример 2: Параметризованные тесты

```python
import pytest

def is_palindrome(text):
    """Проверяет, является ли строка палиндромом"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

@pytest.mark.parametrize("text,expected", [
    ("radar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("python", False),
    ("", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
```

---

## 🚀 Запуск тестов

```bash
# Запустить все тесты
pytest

# Запустить конкретный файл
pytest test_calculator.py

# Запустить конкретный тест
pytest test_calculator.py::test_add

# С подробным выводом
pytest -v

# Показать print в тестах
pytest -s

# Остановиться на первой ошибке
pytest -x

# Показать покрытие кода
pytest --cov=your_module
```

---

## 💡 Лучшие практики

### ✅ Рекомендуется

```python
# 1. Один тест проверяет одну функциональность
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

# 2. Понятные названия тестов
def test_user_can_login_with_valid_credentials():
    pass

# 3. Используйте фикстуры для повторяющихся данных
@pytest.fixture
def user():
    return User("test@example.com", "password")

# 4. Тестируйте граничные случаи
def test_divide_by_very_small_number():
    result = divide(1, 0.0001)
    assert result == 10000
```

---

## 📖 Ресурсы для изучения

- [Pytest Documentation](https://docs.pytest.org/)
- [Real Python - Testing in Python](https://realpython.com/python-testing/)

---

[← Вернуться к roadmap](README.md)
