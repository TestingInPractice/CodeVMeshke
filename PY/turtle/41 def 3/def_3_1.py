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

#https://stepik.org/lesson/1768655/step/1 5.41 def 3 Задания
# Нарисовать Составьте процедуру, которая рисует правильный треугольник с заданной длиной стороны, передаваемой в качестве параметра.
# /CodeVMeshke/PY/turtle/41 def 3/def_3_1.py

def draw_equilateral_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)  # угол поворота для правильного треугольника

# Пример вызова процедуры:
draw_equilateral_triangle(150)


# переменная с номером задачи
num=1
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

