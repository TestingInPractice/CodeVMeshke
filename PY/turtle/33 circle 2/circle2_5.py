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
t.speed(speed=4)  # Установка скорости анимации (1 - самая медленная)


#https://stepik.org/lesson/1744606/step/5  5.33 Цикл 2 Задания
# Решение # Нарисовать из центра 5 кругов разного размера
# # На каждом шаге цикла увеличивать радиус.
#/CodeVMeshke/PY/turtle/33 circle 2/circle2_5.py




circle_radius = 25
radius_increment = 20

t.penup()
t.goto(0, 0)
t.pendown()

for index in range(1, 6):  # пропускаем первый пустой цвет
    t.penup()
    t.goto(0, -circle_radius)  # смещаемся вниз на радиус для правильного центра круга
    t.pendown()
    t.circle(circle_radius)
    circle_radius += radius_increment

# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_{num}.ps"
filename_png = f"screenshot_circle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

