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
# https://stepik.org/lesson/1730144/step/3 5.9 Управление Pen + Состояние рисования - Задания 1
# Решение Задание: Опустить ручку, установить толщину линии равной 7, и нарисовать линию до точки (0, 100).
# Использовать команды pendown, pensize и goto.
t.pendown()
t.pensize(7)
t.goto(0, 100)
# переменная с номером задачи
num=3
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

