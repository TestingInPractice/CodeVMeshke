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

# https://stepik.org/lesson/1723060/step/6 5.25 Задания черепашка 2 круг
# Решение Задание Напишите программу на Python с использованием модуля turtle,
# которая рисует круг и закрашивает его выбранным цветом - green.


#/CodeVMeshke/PY/turtle/27 circle/circle_6.py

# Установка цвета заливки
t.fillcolor("green")
# Поднятие пера и переход к стартовой точке (центр круга по X, центр по Y минус радиус)
t.penup()
t.goto(0, -100)
t.pendown()
# Начало заливки
t.begin_fill()
# Рисование круга радиусом 100
t.circle(100)
# Завершение заливки
t.end_fill()



# переменная с номером задачи
num=6
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

