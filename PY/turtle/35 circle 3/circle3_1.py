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
t.speed(speed=4)  # Установка скорости анимации (1 - самая медленная)
# Решение. Напишите программу на Python с использованием модуля turtle, которая рисует несколько одинаковых квадратов в разных местах рабочего поля, используя цикл for.

side = 60
positions = [(-150, 100), (-50, 50), (50, 0), (150, -50), (250, -100)]

for pos in positions:
    x = pos[0] - side / 2  # левый верхний угол по X
    y = pos[1] + side / 2  # левый верхний угол по Y
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(side)
        t.right(90)
# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle{num}.ps"
filename_png = f"screenshot_circle{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

