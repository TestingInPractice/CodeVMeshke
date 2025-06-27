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


square_size = 10
gap = 10
rows = 4
cols = 4

# Начальная позиция (сдвинем черепашку в левый верхний угол)
start_x = - (cols * (square_size + gap)) / 2
start_y = (rows * (square_size + gap)) / 2

t.penup()
t.goto(start_x, start_y)
t.pendown()

for row in range(rows):
    for col in range(cols):
        # Рисуем квадрат
        for _ in range(4):
            t.forward(square_size)
            t.right(90)
        # Сдвигаемся вправо на размер квадрата + зазор
        t.penup()
        t.forward(square_size + gap)
        t.pendown()
    # Переходим к началу следующей строки
    t.penup()
    t.goto(start_x, start_y - (row + 1) * (square_size + gap))
    t.pendown()

# переменная с номером задачи
num=12
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

