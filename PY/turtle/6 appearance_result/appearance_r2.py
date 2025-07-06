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
# https://stepik.org/lesson/1707358/step/3 5.12 Внешний вид
# Решение Задание: Установить режим изменения размера формы на "user".
# Изменить размер черепахи с помощью shapesize, чтобы сделать её шире (2) и длиннее(3). Использовать shape+forward
t.color("blue", "yellow")

t.resizemode("user")
t.shapesize(stretch_wid=2, stretch_len=3)
t.forward(100)

# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_appearance_r{num}.ps"
filename_png = f"screenshot_appearance_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

