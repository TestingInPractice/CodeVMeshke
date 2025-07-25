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
# https://stepik.org/lesson/1723059/step/6 5.22 Задания черепашка 1 простые фигуры
# Решение Задание:
# Нарисовать квадрат со стороной 50, повернутый на 45 градусов относительно вертикали.
# Используйте команды:
# t.setheading(angle), t.forward(distance), t.right(angle)

#/CodeVMeshke/PY/turtle/5.22 simple fig 1/sf6.py
t.setheading(45)    # Повернуть на 45 градусов относительно вертикали
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)




# переменная с номером задачи
num=6
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf1_r{num}.ps"
filename_png = f"screenshot_sf1_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)