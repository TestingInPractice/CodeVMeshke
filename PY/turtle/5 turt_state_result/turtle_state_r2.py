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
# https://stepik.org/lesson/1707356/step/3 5.11 Состояние черепахи Видимость
# Решение Задание: Сделать черепаху невидимой.
# Переместиться в точку (100, 100), показать черепаху. Использовать hideturtle+goto+showturtle
t.color("blue", "yellow")

t.hideturtle()  # или t.ht()
t.goto(100, 100)
t.showturtle()


# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_turtle_state_r{num}.ps"
filename_png = f"screenshot_turtle_state_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

