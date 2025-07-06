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
# Нарисовать # Куб y = x^3
# /CodeVMeshke/PY/turtle/38 grafix func/graf_func_8.py


t.color("darkblue")
t.penup()
x = -10
step = 3
while x <= 10:
    y = (x) ** 3
    t.goto(x * 5, y)
    if x == -10:
        t.pendown()
    x += step
t.penup()

# переменная с номером задачи
num=8
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

