import turtle
from PIL import Image
import os
# Настройки окна
turtle.setup(800, 600)
turtle.bgpic("auto_grid.gif")  # файл сетки
turtle.title("Код в мешке")
# Настройки черепашки
t = turtle.Turtle()
t.shape("turtle")
t.speed(speed=1)  # Установка скорости анимации (1 - самая медленная)

# https://stepik.org/lesson/1747821/step/3 5.27 Задания черепашка 5
# Решение Задание Напишите программу на Python с использованием модуля turtle,
# которая рисует крест 100 на 100 с серединой в точке (50;50)

#/CodeVMeshke/PY/turtle/27 tasks 5/tasks_3.py
t.penup()
t.goto(0, 50)
t.pendown()      # Опускаем перо — рисуем отрезок
t.forward(100)    # Рисуем линию длиной 20 шагов
t.penup()        # Поднимаем перо — не рисуем
t.goto(50, 100)
t.right(90)
t.pendown()
t.forward(100)    # Перемещаемся вперёд на 20 шагов (пробел)

# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_tasks_{num}.ps"
filename_png = f"screenshot_tasks_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

