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
# Решение Задание 2: Управление параметрами пера и проверка состояния
# Инструкция:
# Сохранить текущие параметры пера в словарь.
# Изменить параметры пера: цвет линии — красный, цвет заливки — зелёный, толщина — 4, показать черепашку, опустить ручку.
# Проверить, опущена ли ручка с помощью isdown().
# Написать на рабочей области состояние.
# Пройти вперед на 150
# Вернуться в дом
# Восстановить сохранённые параметры пера.
# Пройти назад на 150
# Вернуться в дом
pen_settings = t.pen()  # сохранить параметры пера
t.pen(pencolor="red", fillcolor="green", pensize=4, shown=True, pendown=True)
t.write(t.isdown())
t.forward(150)
t.home()
t.pen(pen_settings)
t.backward(150)
t.home()

# переменная с номером задачи
num=2
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

