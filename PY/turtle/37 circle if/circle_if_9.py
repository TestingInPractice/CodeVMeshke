import turtle
import random

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


#https://stepik.org/lesson/1744604/step/4 5.37 Цикл с условием
# # Решение Нарисовать звезду из 8 лучей — 4 больших и 4 малых с помощью цикла
#/CodeVMeshke/PY/turtle/37 circle if/circle_if_9.py


num_rays = 8
big_length = 100
small_length = 50
angle = 360 / num_rays


for i in range(num_rays):
    t.penup()
    t.goto(100,100)
    t.pendown()
    if i % 2 == 0:
        t.forward(big_length)
    else:
        t.forward(small_length)
    t.penup()
    t.goto(100,100)
    t.right(angle)

# переменная с номером задачи
num=9
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_if_{num}.ps"
filename_png = f"screenshot_circle_if_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

