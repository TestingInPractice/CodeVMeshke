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

side = 50
side_increment = 20

for i in range(1, 6):  # пропускаем пустой цвет с индексом 0
    t.color(colors[i])
    t.penup()
    # Смещаемся в левый верхний угол квадрата, чтобы центр квадрата был в (0,0)
    t.goto(-side / 2, -side / 2)
    t.pendown()
    for _ in range(4):
        t.forward(side)
        t.left(90)
    side += side_increment

# переменная с номером задачи
num=7
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

