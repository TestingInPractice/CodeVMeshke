import turtle
from PIL import Image
import os
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

# 1. Управление клавишами
def forward():
    t.forward(50)
def left():
    t.left(45)
def right():
    t.right(45)
def clear():
    t.clear()
def random_color():
    t.color(random.random(), random.random(), random.random())

screen.listen()
screen.onkeypress(forward, "Up")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(clear, "space")
screen.onkeypress(random_color, "r")

# 2. Клик мышью - перемещение черепахи
def goto_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
screen.onscreenclick(goto_click)

# 3. Таймер - шаг вперёд каждые 3 секунды
def auto_step():
    t.forward(20)
    screen.ontimer(auto_step, 3000)
auto_step()

# 4. Запуск главного цикла событий
turtle.done()

# переменная с номером задачи
num=3
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