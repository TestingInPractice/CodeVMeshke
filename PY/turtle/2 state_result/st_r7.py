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
# https://stepik.org/lesson/1728905/step/7  5.7 Сказать состояние черепахе + Настройка и измерение -Задания 1
# Решение Задание:Перейти в координаты (30, 40).
# Вывести расстояние от текущей позиции до точки (0, 0) на экран. Использовать goto+distance+ write+home

t.goto(30,40)
t.write(t.distance(0,0))
t.home()
# переменная с номером задачи
num=7
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_st_r{num}.ps"
filename_png = f"screenshot_st_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

