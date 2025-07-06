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

# https://stepik.org/lesson/1723059/step/9 5.22 Задания черепашка 1 простые фигуры
# Решение Задание:
# Нарисовать половину квадрата.
# Выполнить следующие действия:
# Повернуть черепашку направо на 90 градусов
# Двигаться вперед на 100 шагов (пикселей)
# Повернуть черепашку налево на 90 градусов
# Двигаться назад на 100 шагов
# Используйте команды:
# t.right(angle), t.forward(distance), t.left(angle), t.backward(distance)

#/CodeVMeshke/PY/turtle/5.22 simple fig 1/sf9.py
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)






# переменная с номером задачи
num=9
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