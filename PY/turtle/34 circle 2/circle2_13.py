import turtle
import math
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
# Решение


side = 20       # длина стороны квадрата
gap = 10        # зазор между квадратами
rows = 4
cols = 4

# Длина диагонали квадрата (ширина ромба)
diag = side * math.sqrt(2)

# Начальная позиция (центрируем сетку)
start_x = - (cols * (diag + gap)) / 2
start_y = (rows * (diag + gap)) / 2

t.penup()
t.goto(start_x, start_y)
t.pendown()

for row in range(rows):
    for col in range(cols):
        # Повернуть черепашку на 45 градусов перед рисованием квадрата
        t.setheading(45)
        t.begin_fill()
        for _ in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()
        # Вернуть направление в 0 градусов (вправо)
        t.setheading(0)

        t.penup()
        # Сдвинуться вправо на диагональ + зазор
        t.forward(diag + gap)
        t.pendown()
    # Переход к началу следующей строки
    t.penup()
    t.goto(start_x, start_y - (row + 1) * (diag + gap))
    t.pendown()

# переменная с номером задачи
num=13
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_free1_1{num}.ps"
filename_png = f"screenshot_free1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

