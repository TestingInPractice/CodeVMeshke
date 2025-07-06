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

# https://stepik.org/lesson/1723060/step/7 5.25 Задания черепашка 2 круг
# Решение Задание Напишите программу на Python с использованием модуля turtle,
# которая рисует шесть кругов радиусом 100, каждый из которых повёрнут относительно предыдущего на 60 градусов.

#/CodeVMeshke/PY/turtle/27 circle/circle_7.py
t.left(90)
t.circle(100)
t.right(60)
t.circle(100)
t.right(60)
t.circle(100)
t.right(60)
t.circle(100)
t.right(60)
t.circle(100)
t.right(60)
t.circle(100)


# переменная с номером задачи
num=7
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_{num}.ps"
filename_png = f"screenshot_circle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

