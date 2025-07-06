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

#https://stepik.org/lesson/1757671/step/2 5.34 Цикл 3 Задания
# Решение. Напишите программу на Python с использованием модуля turtle, которая с помощью вложенных циклов for нарисует квадрат, повторяя команды:
# Внешний цикл повторяется 4 раза.
# Внутренний цикл повторяется 4 раза, выполняя команды:
#/CodeVMeshke/PY/turtle/34 circle 3/circle3_2.py



for _ in range(4):          # Внешний цикл повторяется 4 раза
    for _ in range(4):      # Внутренний цикл повторяется 4 раза
        t.forward(40)       # Вперёд 40 шагов
        t.right(90)         # Поворот направо 90 градусов
    t.left(90)              # Поворот налево 90 градусов после внутреннего цикла
# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle{num}.ps"
filename_png = f"screenshot_circle{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

