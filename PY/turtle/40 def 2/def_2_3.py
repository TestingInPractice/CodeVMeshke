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


#https://stepik.org/lesson/1768652/step/3 5.40 def 2 Задания
# Нарисовать Нарисуйте 10 квадратов, каждый следующий повернут на 15 градусов относительно предыдущего и сдвинут вперёд на 10 шагов, чтобы получилась спираль.
# /CodeVMeshke/PY/turtle/40 def 2/def_2_3.py


def draw_square():
    for _ in range(4):
        t.forward(50)
        t.left(90)

for _ in range(10):
    draw_square()
    t.left(15)      # поворот на 15 градусов
    t.penup()
    t.forward(10)   # сдвиг вперёд на 10 шагов
    t.pendown()

# переменная с номером задачи
num=3
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

