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

#https://stepik.org/lesson/1768652/step/7 5.40 def 2 Задания
# Нарисовать Нарисовать 9 маленьких кругов, расположенных квадратом 3×3 (три ряда по три круга).
# /CodeVMeshke/PY/turtle/40 def 2/def_2_7.py

def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)  # Смещаем вниз на радиус, чтобы центр был в (x, y)
    t.pendown()
    t.circle(radius)


radius = 20      # радиус маленьких кругов
spacing = 50     # расстояние между центрами кругов

for row in range(3):
    for col in range(3):
        x = col * spacing
        y = row * spacing
        draw_circle(x, y, radius)


# переменная с номером задачи
num=7
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

