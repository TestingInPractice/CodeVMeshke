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
# Решение
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(3)

#Нарисовать рандомные квадраты

colors = ["red", "green", "blue", "orange", "purple", "cyan"]

for _ in range(12):
    size = random.randint(20, 80)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(colors)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(4):
        t.forward(size)
        t.right(90)

    t.end_fill()


# переменная с номером задачи
num=8
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

