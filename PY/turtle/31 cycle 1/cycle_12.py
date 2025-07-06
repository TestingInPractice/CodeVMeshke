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
#https://stepik.org/lesson/1744607/step/9  5.31 Цикл + задания for без условия
# Решение Нарисовать фигуру из 12 лучей длиной 100 пикселей, исходящих из одной точки
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_12.py

length = 100
for _ in range(12):
    t.forward(length)
    t.backward(length)
    t.left(30)  # 360° / 12 = 30°



# переменная с номером задачи
num=12
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cycle_{num}.ps"
filename_png = f"screenshot_cycle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

