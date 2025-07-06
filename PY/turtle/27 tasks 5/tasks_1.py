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

# https://stepik.org/lesson/1747821/step/1 5.27 Задания черепашка 5
# Решение Задание Черепашка должна нарисовать отрезок длиной 150 шагов, а затем переместиться в середину этого отрезка.
# Чтобы линия была видна начальная точка  t.goto(0, 50).
# Использовать команды penup, goto, pendown, forward и backward.

#/CodeVMeshke/PY/turtle/27 tasks 5/tasks_1.py
t.penup()
t.goto(0, 50)
t.pendown()
t.forward(150)    # Рисуем отрезок длиной 150 шагов
t.penup()         # Поднимаем перо, чтобы не рисовать при перемещении
t.backward(150/2)    # Возвращаемся на середину отрезка
t.pendown()       # Опускаем перо


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_tasks_{num}.ps"
filename_png = f"screenshot_tasks_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

