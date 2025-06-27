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
# Решение

colors = ['', 'purple', 'orange', 'cyan', 'magenta', 'lime']

side_length = 30
increment = 20

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(1, 6):  # пропускаем пустой цвет с индексом 0
    t.color(colors[i])
    for _ in range(4):
        t.forward(side_length)
        t.left(90)
    t.penup()
    t.goto(0, -increment * i)  # смещаемся вниз, чтобы квадраты не накладывались
    t.pendown()
    side_length += increment

# переменная с номером задачи
num=6
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_free1_1{num}.ps"
filename_png = f"screenshot_free1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

