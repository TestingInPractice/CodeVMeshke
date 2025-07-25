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
# https://stepik.org/lesson/1730144/step/4 5.9 Управление Pen + Состояние рисования - Задания 1
# Решение Задание: Переместиться в точку (100, 100), узнать текущую толщину линии и вывести её на экран с помощью черепашки (использовать pensize, goto и write).
# После вывода вернуться в центр с помощью home.
t.goto(100, 100)
t.write(t.pensize())
t.home()
# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_pen_t_r{num}.ps"
filename_png = f"screenshot_pen_st_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

