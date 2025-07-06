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
#https://stepik.org/lesson/1744607/step/5  5.31 Цикл + задания for без условия
# Решение Нарисовать 5 параллельных вертикальных линий длиной 100 пикселей на одинаковом расстоянии 30 пикселей.
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_8.py

t.left(90)
for i in range(1, 6):
    t.pendown()
    t.forward(i * 30)  # длина линии увеличивается с каждым шагом
    t.penup()
    t.backward(i * 30)
    t.left(90)
    t.forward(30)
    t.right(90)



# переменная с номером задачи
num=8
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cycle_{num}.ps"
filename_png = f"screenshot_cycle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

