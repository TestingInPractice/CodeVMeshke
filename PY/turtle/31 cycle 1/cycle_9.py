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

#https://stepik.org/lesson/1744607/step/6  5.31 Цикл + задания for без условия
# Решение Нарисовать пунктирную линию из 10 одинаковых штрихов с пробелами, где длина штриха
# и пробела задаётся переменной length=15. Использовать цикл и команды forward, penup, pendown.
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_9.py


length = 15

t.penup()
t.goto(0, 50)
t.pendown()

for _ in range(10):
    t.forward(length)   # рисуем штрих длиной length
    t.penup()
    t.forward(length)   # делаем пробел той же длины
    t.pendown()




# переменная с номером задачи
num=9
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

