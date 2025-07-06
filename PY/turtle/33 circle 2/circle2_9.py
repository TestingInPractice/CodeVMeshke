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
t.speed(speed=4)  # Установка скорости анимации (1 - самая медленная)

#https://stepik.org/lesson/1744606/step/9  5.33 Цикл 2 Задания
# Решение Напишите программу на Python с использованием модуля turtle, которая последовательно выводит на экран числа из заданного списка
# [8, 10, 12, 14, 16] перемещаясь вперёд на фиксированное расстояние (30) после каждой записи.
#/CodeVMeshke/PY/turtle/33 circle 2/circle2_9.py


t.pencolor("blue")
t.pensize(3)
t.penup()

for step in [8, 10, 12, 14, 16]:  # новый список значений для переменной step
    t.write(step)  # написать текущее значение переменной step
    t.forward(30)

# переменная с номером задачи
num=9
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_free1_1{num}.ps"
filename_png = f"screenshot_free1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

