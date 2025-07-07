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


#https://stepik.org/lesson/1768652/step/4 5.40 def 2 Задания
# Нарисовать Крест из квадратов Нарисуйте 5 квадратов со стороной 50: один в центре, и по одному сверху, снизу, слева и справа от него, образуя крест.
# /CodeVMeshke/PY/turtle/40 def 2/def_2_4.py


def draw_square():
    for _ in range(4):
        t.forward(50)
        t.left(90)

# Координаты центров квадратов для креста
positions = [
    (0, 0),          # центр
    (0, 60),         # сверху
    (0, -60),        # снизу
    (-60, 0),        # слева
    (60, 0)          # справа
]

for x, y in positions:
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_square()

# переменная с номером задачи
num=4
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

