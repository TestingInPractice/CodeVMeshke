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
# Решение
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(3)

def draw_square():
    for _ in range(4):
        t.forward(50)
        t.left(90)

for i in range(4):
    t.penup()
    t.goto(i * 100, 0)
    t.pendown()
    if i % 2 == 1:  # нечётные квадраты
        t.setheading(45)
    else:  # чётные квадраты
        t.setheading(0)
    draw_square()
    t.setheading(0)  # сброс направления для следующего квадрата

# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_2_{num}.ps"
filename_png = f"screenshot_def_2_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

