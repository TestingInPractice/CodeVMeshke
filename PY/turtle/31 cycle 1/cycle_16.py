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

#https://stepik.org/lesson/1744607/step/13  5.31 Цикл + задания for без условия
# Решение Нарисовать три одинаковых треугольника со стороной 100 пикселей, расположенных в ряд, используя цикл и команды модуля turtle: forward и left. 
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_16.py

length = 100
spacing = 0  # расстояние между треугольниками

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(3):  # например, 3 треугольника
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.penup()
    t.forward(length + spacing)  # сдвигаемся вправо для следующего треугольника
    t.pendown()

# переменная с номером задачи
num=16
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

