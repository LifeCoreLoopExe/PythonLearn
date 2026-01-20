# import tkinter as tk
# from tkinter import ttk
# import math
# from playsound import playsound
# import threading
#
# # Создаем основное окно
# root = tk.Tk()
# root.title("Калькулятор")
# root.geometry("430x290")
# root.resizable(False, False)
#
# # Управление выражением
# def is_valid_expression(expr):
#     if not expr:
#         return False
#     # Проверяем, что выражение не содержит букв и не заканчивается оператором
#     if any(c.isalpha() for c in expr):
#         return False
#     if expr[-1] in "+-*/.=√%" or ".." in expr:
#         return False
#     return True
#
# # Функции для кнопок
# def button_click(value):
#     current = entry_var.get()
#     # Предотвращение повторяющихся операторов
#     if current and current[-1] in "+-*/.√%" and value in "+-*/.√%":
#         return
#     entry_var.set(current + str(value))
#
# def clear_display():
#     entry_var.set("")
#
# def calculate():
#     expr = entry_var.get()
#     if not is_valid_expression(expr):
#         entry_var.set("Ошибка")
#         return
#     try:
#         result = eval(expr)
#         entry_var.set(str(result))
#     except Exception:
#         entry_var.set("Ошибка")
#
# def sqrt_action():
#     current = entry_var.get()
#     try:
#         # Если есть число — извлекаем корень
#         if current:
#             value = float(current)
#             if value < 0:
#                 entry_var.set("Ошибка")
#             else:
#                 result = math.sqrt(value)
#                 entry_var.set(str(result))
#         else:
#             entry_var.set("Ошибка")
#     except:
#         entry_var.set("Ошибка")
#
# def backspace_action():
#     current = entry_var.get()
#     if current:
#         entry_var.set(current[:-1])  # Удаляем последний символ
#
# def percent_action():
#     current = entry_var.get()
#     try:
#         if current:
#             value = float(current)
#             # 1% от числа
#             result = value * 0.01
#             entry_var.set(str(result))
#         else:
#             entry_var.set("Ошибка")
#     except:
#         entry_var.set("Ошибка")
# # Звуки для кнопок
# def play_sound():
#     threading.Thread(target=playsound, args=("click_sound.mp3",)).start()
#
# # Анимация кнопок
# def animate_button_press(button):
#     button['style'] = "Pressed.TButton"
#     root.after(100, lambda: button.config(style="TButton"))
#
# # Основной дисплей калькулятора
# entry_var = tk.StringVar()
# entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 25), justify="right")
# entry.grid(row=0, column=0, columnspan=8, padx=15, pady=15)
#
# # Кнопки
# buttons = [
#     ("C", 1, 0, "clear"), ("(", 1, 2), (")", 1, 3), ("/", 1, 4),
#     ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
#     ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
#     ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
#     ("0", 5, 0), (".", 5, 1), ("=", 5, 2, "eval"),
#     ("√", 5, 3, "sqrt"), ("%", 2, 4, "percent"), ("←", 1, 1, "backspace")
# ]
#
# # Стили для кнопок
# style = ttk.Style()
# style.configure("TButton", font=("Arial", 14), width=6)
#
# for btn_text, row, col, *action in buttons:
#     cmd = (calculate if action and action[0] == "eval" else
#            clear_display if action and action[0] == "clear" else
#            sqrt_action if action and action[0] == "sqrt" else
#            backspace_action if action and action[0] == "backspace" else
#            percent_action if action and action[0] == "percent" else
#            lambda v=btn_text: button_click(v))
#     ttk.Button(root, text=btn_text, command=cmd).grid(row=row, column=col, padx=5, pady=5)
#
# # Ограничение ввода букв
# def validate_input(*args):
#     expr = entry_var.get()
#     if any(c.isalpha() for c in expr):
#         entry_var.set("".join(c for c in expr if not c.isalpha()))
#
# entry_var.trace("w", validate_input)
#
# # Запуск основного цикла
# root.mainloop()

from playsound3 import playsound
import tkinter as tk
from tkinter import ttk
import threading

# Создаем основное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("545x300")
root.resizable(False, False)

# Управление выражением
def is_valid_expression(expr):
    if not expr:
        return False
    if any(c.isalpha() for c in expr):
        return False
    if expr[-1] in "+-*/.=←√%" or ".." in expr:
        return False
    return True

# Функции для кнопок
def button_click(value):
    current = entry_var.get()
    if current and current[-1] in "+-*/.←√%" and value in "+-*/.←√%":
        return
    entry_var.set(current + str(value))

def clear_display():
    entry_var.set("")

def calculate():
    expr = entry_var.get()
    if not is_valid_expression(expr):
        entry_var.set("Ошибка")
        return
    try:
        result = eval(expr)
        entry_var.set(str(result))
    except Exception:
        entry_var.set("Ошибка")

# Функция для вычисления корня
def calculate_sqrt():
    try:
        value = float(entry_var.get())
        if value < 0:
            entry_var.set("Ошибка")
            return
        result = math.sqrt(value)
        entry_var.set(str(result))
    except Exception:
        entry_var.set("Ошибка")

# Функция для вычисления процента
def calculate_percent():
    try:
        value = float(entry_var.get())
        result = value / 100
        entry_var.set(str(result))
    except Exception:
        entry_var.set("Ошибка")

# Функция для удаления последнего символа
def backspace():
    current = entry_var.get()
    if len(current) > 0:
        entry_var.set(current[:-1])


# Звуки для кнопок
def play_sound():
    threading.Thread(target=playsound, args=("240873eb7fa092b.mp3",)).start()

# Анимация кнопок
def animate_button_press(button):
    button['style'] = "Pressed.TButton"
    root.after(100, lambda: button.config(style="TButton"))

# Основной дисплей калькулятора
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 35), justify="right")
entry.grid(row=0, column=0, columnspan=60, padx=10, pady=10)

# Стили для кнопок
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), width=8, relief="flat")
style.map("TButton",
          background=[("pressed", "lightgray"), ("active", "white")],
          foreground=[("pressed", "black"), ("active", "blue")])

style.configure("Pressed.TButton", background="gray", foreground="white")

# Кнопки
buttons = [
    ("C", 1, 0, "clear"), ("(", 1, 2), (")", 1, 3), ("/", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2, "eval"),
    ("←", 1, 1, "backspace"), ("√", 5, 3, "sqrt"), ("%", 2, 4, "percent")
]

# Генерация кнопок
for btn_text, row, col, *action in buttons:
    cmd = (calculate if action and action[0] == "eval" else
           clear_display if action and action[0] == "clear" else
           backspace if action and action[0] == "backspace" else
           calculate_sqrt if action and action[0] == "sqrt" else
           calculate_percent if action and action[0] == "percent" else
           lambda v=btn_text: button_click(v))
    button = ttk.Button(root, text=btn_text, command=lambda b=btn_text, bt=cmd: [bt(), play_sound(), animate_button_press(button)])
    button.grid(row=row, column=col, padx=5, pady=5)

# Ограничение ввода букв
def validate_input(*args):
    expr = entry_var.get()
    if any(c.isalpha() for c in expr):
        entry_var.set("".join(c for c in expr if not c.isalpha()))

entry_var.trace("w", validate_input)

# Запуск основного цикла
root.mainloop()