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

#https://stepik.org/lesson/1744609/step/2  5.30 Условия If
# Решение Напишите программу на Python с использованием модуля turtle, которая:
# Запрашивает у пользователя длину стороны линии через диалоговое окно.
# Если введённое число больше 100, рисует линию синего цвета длиной, равной введённому числу.
# Если введённое число меньше или равно 100, рисует линию красного цвета длиной в два раза больше введённого числа.

#/CodeVMeshke/PY/turtle/32 condition/cond_2.py

# Запрос длины стороны
side_length = turtle.numinput("Длина стороны", "Введите длину стороны:")

if side_length is not None:
    if side_length > 100:
        t.pencolor("blue")
        t.forward(side_length)
    else:
        t.pencolor("red")
        t.forward(side_length * 2)


# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cond_{num}.ps"
filename_png = f"screenshot_cond_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

