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
t.speed(speed=3)  # Установка скорости анимации (1 - самая медленная)
# Решение


def draw_triangle(x, y, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(5)
    for _ in range(3):
        t.forward(side_length)
        t.left(120)


def draw_square(x, y, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(5)
    for _ in range(4):
        t.forward(side_length)
        t.left(90)


def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)  # центр круга в (x, y)
    t.pendown()
    t.speed(5)
    t.circle(radius)


def draw_x(x, y, size):
    """
    Рисует символ X с центром в (x, y) и длиной линии size.
    """
    t.penup()
    half = size / 2
    # Левая верхняя точка
    t.goto(x - half, y + half)
    t.pendown()
    t.speed(5)
    t.goto(x + half, y - half)
    t.penup()
    # Левая нижняя точка
    t.goto(x - half, y - half)
    t.pendown()
    t.goto(x + half, y + half)


# Фреймворк — словарь с вызовами фигур
shapes = {
    "triangle": draw_triangle,
    "square": draw_square,
    "circle": draw_circle,
    "x": draw_x
}

def draw_shape(shape_name, x, y, size):
    """
    Рисует фигуру shape_name в координатах (x, y) с размером size.
    Для треугольника и квадрата size — длина стороны,
    для круга — радиус,
    для X — длина линии.
    """
    if shape_name in shapes:
        shapes[shape_name](x, y, size)
    else:
        print(f"Фигура '{shape_name}' не поддерживается.")

# Примеры вызова:
draw_shape("triangle", -200, 0, 100)
draw_shape("square", -100, 0, 100)
draw_shape("circle", 50, 50, 50)
draw_shape("x", 150, 50, 100)






# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_3_{num}.ps"
filename_png = f"screenshot_def_3_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

