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


#https://stepik.org/lesson/1744606/step/10  5.33 Цикл 2 Задания
# Решение Напишите программу на Python с использованием модуля turtle, которая последовательно выводит на экран числа
# range(1, 9), перемещаясь вперёд на фиксированное расстояние (30) после каждой записи.
#/CodeVMeshke/PY/turtle/33 circle 2/circle2_10.py


t.pensize(3)
t.penup()

for step in range(1, 9):
    t.write(step)  # написать текущее значение переменной step
    t.forward(30)

# переменная с номером задачи
num=10
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

