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

# https://stepik.org/lesson/1723059/step/2 5.22 Задания черепашка 1 простые фигуры
# Решение Задание:Нарисуйте стрелку, как на рисунке. Начальная точка — центр координат (0, 0). Используйте только команды forward, left, right, penup, pendown, goto. Размеры и углы подберите по изображению.

t.penup()
t.goto(0, 100)      # Старт: верхняя вершина треугольника
t.pendown()
t.goto(-100, 0)     # Левая вершина треугольника
t.goto(0, -100)     # Нижняя вершина треугольника
t.goto(0, -50)     # Нижняя вершина треугольника
t.penup()
t.goto(0, -50)     # Нижняя вершина треугольника
t.pendown()
t.goto(0, 100)      # Замыкаем треугольник
t.penup()
t.goto(0, 50)    # Верх квадрата вправо
t.pendown()
t.goto(100, 50)    # Верх квадрата вправо
t.goto(100, -50)   # Вниз по правой стороне квадрата
t.goto(0, -50)     # Влево по низу квадрата




# переменная с номером задачи
num=2
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