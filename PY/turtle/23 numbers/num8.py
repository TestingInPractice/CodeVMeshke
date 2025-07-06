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

# https://stepik.org/lesson/1747822/step/8 5.23 Задания черепашка Цифры
# Решение Задание: Нарисовать цифру «8» почтовым стилем


# /CodeVMeshke/PY/turtle/23 numbers/num8.py
t.penup()
t.goto(0, 100)      # Начинаем в верхнем левом углу цифры
t.pendown()
t.forward(50)       # Верхняя горизонтальная линия
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.penup()
t.goto(0, 50)
t.pendown()
t.right(90)
t.forward(50)




# переменная с номером задачи
num=8
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_num_r{num}.ps"
filename_png = f"screenshot_num_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)