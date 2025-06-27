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

fill_colors = ['purple', 'orange', 'cyan', 'magenta', 'lime']

side = 50
side_increment = 20

# Сначала рисуем самый большой квадрат и заливаем его внешним цветом
for i in range(4, -1, -1):  # от 4 до 0
    t.penup()
    t.goto(- (side + side_increment * i) / 2, - (side + side_increment * i) / 2)
    t.pendown()
    t.fillcolor(fill_colors[i])
    t.begin_fill()
    for _ in range(4):
        t.forward(side + side_increment * i)
        t.left(90)
    t.end_fill()

# переменная с номером задачи
num=8
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

