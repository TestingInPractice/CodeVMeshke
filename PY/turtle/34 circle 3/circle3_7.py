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
t.speed(speed=4)  # Установка скорости анимации (1 - самая медленная)

#https://stepik.org/lesson/1757671/step/7 5.34 Цикл 3 Задания
# Решение. Нарисуйте два круга с помощью модуля turtle на Python, расположенных рядом по горизонтали.
#/CodeVMeshke/PY/turtle/34 circle 3/circle3_7.py

t.pencolor("green")
t.pensize(2)
t.left(90)

for step in range(360):
    t.forward(1)
    t.right(1)

t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

for step in range(360):
    t.forward(1)
    t.right(1)
# переменная с номером задачи
num=7
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle{num}.ps"
filename_png = f"screenshot_circle{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

