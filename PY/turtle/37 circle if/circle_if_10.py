import turtle
import random

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



#https://stepik.org/lesson/1744604/step/5 5.37 Цикл с условием
# #Нарисовать Напишите программу на Python с использованием модуля turtle, которая рисует 6 одинаковых квадратов в ряд
#/CodeVMeshke/PY/turtle/37 circle if/circle_if_10.py



side = 40
gap = 10

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(6):
    t.penup()
    t.goto(i * (side + gap), 0)
    t.pendown()
    if i % 2 == 1:  # если номер квадрата нечётный (второй, четвёртый, шестой)
        t.fillcolor('black')
        t.begin_fill()
    else:
        t.fillcolor('white')
        t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()





# переменная с номером задачи
num=10
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_if_{num}.ps"
filename_png = f"screenshot_circle_if_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

