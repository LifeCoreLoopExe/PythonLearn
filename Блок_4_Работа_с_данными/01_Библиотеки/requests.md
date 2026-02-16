# 🌐 Библиотека requests

[← Вернуться к roadmap](README.md)

---

## 🎯 Цель изучения

Научиться работать с HTTP-запросами используя библиотеку requests.

---

## 📚 Теория

### Установка

```bash
pip install requests
```

### Базовые запросы

```python
import requests

# GET запрос
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())       # Автоматический парсинг JSON

# POST запрос
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://example.com/login', json=data)

# Параметры запроса
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.example.com/search', params=params)

# Заголовки
headers = {'Authorization': 'Bearer TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Обработка ответов

```python
response = requests.get('https://api.github.com')

# Статус
print(response.status_code)  # 200
print(response.ok)           # True if status < 400

# Содержимое
print(response.text)         # Текст ответа
print(response.json())       # JSON в dict
print(response.content)      # Бинарное содержимое

# Заголовки
print(response.headers)
print(response.headers['Content-Type'])
```

---

## 💻 Практические примеры

### Пример 1: Получение погоды

```python
import requests

def get_weather(city):
    """Получает погоду для города"""
    # Пример с OpenWeatherMap API
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Вызывает ошибку для плохих статусов
        
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        
        print(f"🌡️ Погода в {city}:")
        print(f"Температура: {temp}°C")
        print(f"Описание: {desc}")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка запроса: {e}")

get_weather("Москва")
```

### Пример 2: Скачивание файла

```python
import requests

def download_file(url, filename):
    """Скачивает файл по URL"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"✅ Файл скачан: {filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка: {e}")

download_file('https://example.com/image.jpg', 'image.jpg')
```

---

## 📖 Ресурсы для изучения

- [Requests Documentation](https://requests.readthedocs.io/)
- [Real Python - Python Requests](https://realpython.com/python-requests/)

---

[← Вернуться к roadmap](README.md)
