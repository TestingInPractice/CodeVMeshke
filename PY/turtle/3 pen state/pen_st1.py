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
# https://stepik.org/lesson/1707355/step/2 5.8 Управление Pen + Состояние рисования
# Решение Задание 1: Управление состоянием ручки и толщиной линии
# Шаги:
# Поднять ручку с помощью penup(), pu() или up().
# Переместиться в точку (-100, 0) без рисования линии.
# Опустить ручку с помощью pendown(), pd() или down().
# Установить толщину линии 7 с помощью pensize() или width().
# Нарисовать линию вперёд на 150 шагов.
# Поднять ручку с помощью penup()
# Вернуться в дом
t.penup() # или t.pu(), t.up()
t.goto(-100, 0)
t.pendown() # или t.pd(), t.down()
t.pensize(7)  # или t.width(7)
t.forward(150)
t.penup()
t.home()

# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_pen_st{num}.ps"
filename_png = f"screenshot_pen_st{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

