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

# https://stepik.org/lesson/1757670/step/6 5.24 Задания черепашка 2 простые фигуры
# Решение Напишите программу, которая с помощью черепашки нарисует дом. Основание Y = 50.
# Добавляем перекрестье в нижней части дома и горизонтальную линию, отсоедииняющую крышу.
# Установить цвет пера красный и цвет заливки жёлтый

#/CodeVMeshke/PY/turtle/24 simple fig 2/sf_r6.py
t.penup()
# Начинаем с точки
t.goto(-50, 50)
t.pendown()

# Соединяем точки
t.goto(-50, 90)
t.goto(0, 110)
t.goto(50, 90)
t.goto(50, 50)
t.goto(-50, 50)

# Рисуем перекрестье в нижнем прямоугольнике
t.penup()
t.goto(-50, 50)
t.pendown()
t.goto(50, 90)

t.goto(-50, 90)

t.goto(50, 50)



# переменная с номером задачи
num=6
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf_r{num}.ps"
filename_png = f"screenshot_sf_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

