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

t.speed(10)
t.pensize(2)
t.color("black", "cyan")  # цвет линии и заливки

side = 50  # длина катетов прямоугольного треугольника

for _ in range(6):
    t.begin_fill()
    t.forward(side)    # первый катет
    t.left(90)
    t.forward(side)    # второй катет
    t.left(135)
    t.forward(side * (2 ** 0.5))  # гипотенуза (по теореме Пифагора)
    t.left(135)
    t.end_fill()

    t.penup()
    t.forward(side)    # сдвигаемся вправо на длину катета для следующего треугольника
    t.pendown()






# переменная с номером задачи
num=12
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

