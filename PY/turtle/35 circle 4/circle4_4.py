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
t.speed(speed=3)  # Установка скорости анимации (1 - самая медленная)


#https://stepik.org/lesson/1762757/step/4 5.35 Цикл 4 Задания
# Решение. Что нарисует черепашка после выполнения следующей программы на Python?
#/CodeVMeshke/PY/turtle/36 circle 4/circle4_4.py

for _ in range(10):
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(90)
    t.forward(20)
    t.left(90)
# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle4_{num}.ps"
filename_png = f"screenshot_circle4_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

