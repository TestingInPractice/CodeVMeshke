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

#https://stepik.org/lesson/1744605/step/1 5.38 Графики функций
# #Нарисовать  # Парабола с ветвями вверх y = 0.05x^2
# /CodeVMeshke/PY/turtle/38 grafix func/graf_func_3.py


t.color("orange")
t.penup()
x = -100
step = 5
while x <= 100:
    y = 0.05 * x**2
    t.goto(x, y)
    if x == -100:
        t.pendown()
    x += step
t.penup()

# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_graf_func_{num}.ps"
filename_png = f"screenshot_graf_func_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

