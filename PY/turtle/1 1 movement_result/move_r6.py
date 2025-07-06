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
# https://stepik.org/lesson/1724290/step/6 5.4 Двигаться и рисовать - задания 1
# Решение Задание: Повернуть черепаху на 90 градусов право. Использовать right.
t.right(90)
#
# Получаем холст tkinter
canvas = turtle.getcanvas()

# Сохраняем содержимое холста в файл postscript
canvas.postscript(file="screenshot_move_r6.ps", colormode='color')
# Конвертируем postscript в PNG
img = Image.open("screenshot_move_r6.ps")
img.save("screenshot_move_r6.png")
os.remove("screenshot_move_r6.ps")
turtle.done()  #(окно не закрывается сразу)