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

# https://stepik.org/lesson/1757670/step/4 5.24 Задания черепашка 2 простые фигуры
# Решение Задание: Напишите программу, которая с помощью черепашки нарисует трапецию
# с основаниями разной длины и наклонными боковыми сторонами, то есть не прямоугольную трапецию.

# /CodeVMeshke/PY/turtle/24 simple fig 2/sf_r4.py

# Нижнее основание
t.forward(150)

# Левая боковая сторона под углом 45°
t.left(120)
t.forward(70)

# Верхнее основание
t.left(60)
t.forward(80)

# Правая боковая сторона — чтобы замкнуть фигуру
t.left(60)
t.forward(70)


# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf_r{num}.ps"
filename_png = f"screenshot_sf_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

