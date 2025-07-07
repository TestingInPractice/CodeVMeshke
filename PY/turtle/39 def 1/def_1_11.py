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



#https://stepik.org/lesson/1744603/step/5 5.39 функции def
# Нарисовать #Нарисовать три пересекающихся круга пирамидкой
# /CodeVMeshke/PY/turtle/39 def 1/def_1_11.py


radius = 100

def draw_circle_at(x, y, color, radius):
    """Перемещает черепашку в точку (x, y - radius) и рисует круг заданного цвета и радиуса."""
    t.penup()
    t.goto(x, y - radius)  # Смещаемся вниз на радиус, чтобы центр круга был в (x, y)
    t.pendown()
    t.pencolor(color)
    t.circle(radius)

# Вычисляем длину стороны равностороннего треугольника
side = radius * math.sqrt(3)
# Верхний круг (синий)
draw_circle_at(0, radius, "blue", radius)

# Левый нижний круг (красный)
draw_circle_at(-side / 2, -radius / 2, "red", radius)

# Правый нижний круг (зелёный)
draw_circle_at(side / 2, -radius / 2, "green", radius)



# radius = 100
#
# # Вычисляем смещение между центрами (сторона треугольника)
# side = radius * math.sqrt(3)
#
# # Верхний круг (синий)
# t.penup()
# t.goto(0, radius)
# t.pendown()
# t.pencolor("blue")
# t.circle(radius)
#
# # Левый нижний круг (красный)
# t.penup()
# t.goto(-side/2, -radius/2)
# t.pendown()
# t.pencolor("red")
# t.circle(radius)
#
# # Правый нижний круг (зелёный)
# t.penup()
# t.goto(side/2, -radius/2)
# t.pendown()
# t.pencolor("green")
# t.circle(radius)






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

