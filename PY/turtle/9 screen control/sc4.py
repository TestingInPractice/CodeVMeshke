import turtle
from PIL import Image
import os
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

# https://stepik.org/lesson/1727575/step/4 5.15 TurtleScreen Контроль за окном+


screen = turtle.Screen()
t = turtle.Turtle()

# Ввод цвета через текстовое окно
color = screen.textinput("Цвет", "Введите цвет круга (например, red, blue):")
if color is None:
    print("Ввод отменён")
    turtle.bye()
    exit()

# Ввод радиуса через числовое окно
radius = screen.numinput("Радиус", "Введите радиус круга (10-150):", default=50, minval=10, maxval=150)
if radius is None:
    print("Ввод отменён")
    turtle.bye()
    exit()

t.fillcolor(color)
t.begin_fill()
t.circle(radius)
t.end_fill()



# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sс{num}.ps"
filename_png = f"screenshot_sс{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)