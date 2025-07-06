import turtle
from datetime import datetime

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

#https://stepik.org/lesson/1744608/step/5  5.29 Ввод переменных
# Решение Задание
# Напишите программу на Python с использованием модуля turtle, которая:
# Запрашивает у пользователя в диалоговом окне длину стороны треугольника.
# Рисует равносторонний треугольник с указанной длиной стороны на экране.
# /CodeVMeshke/PY/turtle/31 variables/variables_5.py


screen = turtle.Screen()
side_length = screen.numinput("Ввод", "Введите длину стороны треугольника:", minval=10, maxval=300)

if side_length is not None:
#нужен отступ вправо после if
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)

# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_var_{num}.ps"
filename_png = f"screenshot_var_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

