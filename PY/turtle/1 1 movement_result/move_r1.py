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
# Решение Задание: Переместить черепаху на 100 пикселей прямо. Использовать forward.
t.forward(100)
#
# Получаем холст tkinter
canvas = turtle.getcanvas()

# Сохраняем содержимое холста в файл postscript
canvas.postscript(file="screenshot_move_r1.ps", colormode='color')
# Конвертируем postscript в PNG
img = Image.open("screenshot_move_r1.ps")
img.save("screenshot_move_r1.png")
os.remove("screenshot_move_r1.ps")
turtle.done()  #(окно не закрывается сразу)