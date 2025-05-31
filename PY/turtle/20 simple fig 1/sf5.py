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
# Решение  Нарисовать из точки (0, 0) пять лучей длиной 100 единиц с разницей в 45 градусов. Все лучи должны исходить из одной точки.
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.left(45)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.left(45)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.left(45)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.left(45)
t.forward(100)



# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf1_r{num}.ps"
filename_png = f"screenshot_sf1_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)