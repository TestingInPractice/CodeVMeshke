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
t.speed(1)


num_sides = turtle.numinput("Ввод", "Введите число сторон фигуры (3, 4 или 5):", minval=3, maxval=5)

if num_sides is not None:
    num_sides = int(num_sides)
    side_length = 50

    if num_sides == 3:
        # Треугольник
        t.forward(side_length)
        t.left(120)
        t.forward(side_length)
        t.left(120)
        t.forward(side_length)
        t.left(120)

    elif num_sides == 4:
        # Квадрат
        t.forward(side_length)
        t.left(90)
        t.forward(side_length)
        t.left(90)
        t.forward(side_length)
        t.left(90)
        t.forward(side_length)
        t.left(90)

    elif num_sides == 5:
        # Пятиугольник
        t.forward(side_length)
        t.left(72)
        t.forward(side_length)
        t.left(72)
        t.forward(side_length)
        t.left(72)
        t.forward(side_length)
        t.left(72)
        t.forward(side_length)
        t.left(72)





# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cond_{num}.ps"
filename_png = f"screenshot_cond_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

