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
# https://stepik.org/lesson/1707356/step/2 5.10 Управление цветом+Заполнение+Больше контроля рисования
# Решение адание 1: Управление цветом пера и заливки
# Установить цвет пера в красный с помощью pencolor().
# Установить цвет заливки в жёлтый с помощью fillcolor().
# Нарисовать квадрат со стороной 100, заполненный цветом заливки.
# Затем изменить одновременно цвет пера и заливки на синий и зелёный с помощью color().
# Нарисовать круг радиусом 50 с новыми цветами.
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Начать заливку
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
# Переместиться, чтобы не перекрывать фигуры
t.penup()
t.goto(150,     0)
t.pendown()

# Установить цвет пера синий, цвет заливки зелёный
t.color("blue", "green")

# Нарисовать круг с заливкой
t.begin_fill()
t.circle(50)
t.end_fill()
t.home()

# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_color{num}.ps"
filename_png = f"screenshot_color{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

