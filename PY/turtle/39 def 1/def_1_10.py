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

#https://stepik.org/lesson/1744603/step/3 5.39 функции def
# Нарисовать #Нарисовать три касающихся круга разного цвета
# /CodeVMeshke/PY/turtle/39 def 1/def_1_10.py

radius = 50
colors = ["blue", "red", "green"]

def draw_colored_circle(color, radius):
    t.pencolor(color)
    t.circle(radius)

def move_right(distance):
    t.penup()
    t.forward(distance)
    t.pendown()

# Начальная позиция
t.penup()
t.goto(0, 0)
t.pendown()

for color in colors:
    draw_colored_circle(color, radius)
    move_right(2 * radius)



# radius = 50
#
# # Первый круг (синий)
# t.pencolor("blue")
# t.circle(radius)
#
# # Перейти к следующей позиции (правый край первого круга)
# t.penup()
# t.forward(2 * radius)
# t.pendown()
#
# # Второй круг (красный)
# t.pencolor("red")
# t.circle(radius)
#
# # Перейти к следующей позиции (правый край второго круга)
# t.penup()
# t.forward(2 * radius)
# t.pendown()
#
# # Третий круг (зелёный)
# t.pencolor("green")
# t.circle(radius)



# переменная с номером задачи
num=10
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

