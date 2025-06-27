import turtle
from PIL import Image
import math
import os
# Настройки окна
turtle.setup(800, 600)
turtle.bgpic("auto_grid.gif")  # файл сетки
turtle.title("Код в мешке")
# Настройки черепашки
t = turtle.Turtle()
t.shape("turtle")
t.speed(speed=1)  # Установка скорости анимации (1 - самая медленная)
# Решение
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(3)

#

radius = 100

# Вычисляем смещение между центрами (сторона треугольника)
side = radius * math.sqrt(3)

# Верхний круг (синий)
t.penup()
t.goto(0, radius)
t.pendown()
t.pencolor("blue")
t.circle(radius)

# Левый нижний круг (красный)
t.penup()
t.goto(-side/2, -radius/2)
t.pendown()
t.pencolor("red")
t.circle(radius)

# Правый нижний круг (зелёный)
t.penup()
t.goto(side/2, -radius/2)
t.pendown()
t.pencolor("green")
t.circle(radius)






# переменная с номером задачи
num=11
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_1_{num}.ps"
filename_png = f"screenshot_def_1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

