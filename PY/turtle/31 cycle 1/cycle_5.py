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

#https://stepik.org/lesson/1744607/step/2  5.31 Цикл + задания for без условия
# Решение Нарисовать квадрат со стороной 50 пикселей, используя цикл for и только команды forward и left. Проверка регулярным выражением + ожидается 2 строки в теле цикла.
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_4.py

for i in range(4):
    t.forward(50)
    t.left(90)

# переменная с номером задачи
num=5
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

