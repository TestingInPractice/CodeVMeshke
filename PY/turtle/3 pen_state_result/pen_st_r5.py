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
# https://stepik.org/lesson/1730144/step/5 5.9 Управление Pen + Состояние рисования - Задания 1
# Решение Задание: Изменить параметры пера: цвет линии — синий, цвет заливки — зелёный, толщина линии — 4, опустить ручку и показать черепашку.
# Нарисовать круг радиусом 50. Использовать команду pen и circle.
t.pen(pencolor="blue", fillcolor="green", pensize=4, pendown=True, shown=True)
t.circle(50)
# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_pen_t_r{num}.ps"
filename_png = f"screenshot_pen_st_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

