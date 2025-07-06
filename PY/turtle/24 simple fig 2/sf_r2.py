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

# https://stepik.org/lesson/1757670/step/2 5.24 Задания черепашка 2 простые фигуры
# Решение Нарисовать прямоугольник шириной 50 и высотой 100. (Y>0)
# Используйте команды:
# t.forward(distance), t.right(angle)

#/CodeVMeshke/PY/turtle/24 simple fig 2/sf_r2.py
t.forward(100)  # Высота
t.right(90)
t.forward(50)   # Ширина
t.right(90)
t.forward(100)  # Высота
t.right(90)
t.forward(50)   # Ширина


# переменная с номером задачи
num=2
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

