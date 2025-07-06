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
# https://stepik.org/lesson/1724291/step/10 5.5 Двигаться и рисовать - задания 2
# Решение Задание: Оставить отпечаток в координатах 50:50. Оставить отпечаток, отменить отпечаток. Использовать goto + stamp+undo
t.goto(50,50)
t.stamp()
t.undo()
t.home()

# переменная с номером задачи
num=25
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_move_r{num}.ps"
filename_png = f"screenshot_move_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)