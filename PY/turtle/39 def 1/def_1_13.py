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


#https://stepik.org/lesson/1744603/step/6 5.39 функции def
# Нарисовать #Нарисовать несколько многоугольников с использованием функций и цикла. Использовать циклы для упрощения и сокращения кода.
# /CodeVMeshke/PY/turtle/39 def 1/def_1_13.py



def move_to(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()


colors = ['red', 'green', 'blue', 'cyan', 'magenta']
x_positions = [0, 100, -100, 100, -100]
y_positions = [0, 100, -100, -100, 100]

for i in range(len(colors)):
    move_to(x_positions[i], y_positions[i], colors[i])
    draw_polygon(i + 3, 50)  # количество сторон от 3 до 7





# переменная с номером задачи
num=13
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

