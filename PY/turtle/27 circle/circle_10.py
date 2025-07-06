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

# https://stepik.org/lesson/1723060/step/10 5.25 Задания черепашка 2 круг
# Решение Задание
# Нарисуйте зеленую точку диаметром 20 в текущей позиции.
# Поднимите перо, переместите черепашку в координаты (0, -100), опустите перо.
# Нарисуйте зеленый круг радиусом 100.

#/CodeVMeshke/PY/turtle/27 circle/circle_10.py
t.pencolor("green")
t.dot(20)
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)


# переменная с номером задачи
num=1
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

