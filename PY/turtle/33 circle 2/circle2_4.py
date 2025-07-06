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

#https://stepik.org/lesson/1744606/step/4  5.33 Цикл 2 Задания
# Решение Нарисовать три квадрата (сторона 100), расположенных "лесенкой" с
# заходом каждого следующего квадрата на четверть стороны предыдущего. Использовать цикл и команды модуля turtle. Проверка регулярным выражением
#/CodeVMeshke/PY/turtle/33 circle 2/circle2_4.py


side = 100
overlap = side / 4  # заход на четверть стороны

t.penup()
t.goto(0, 0)
t.pendown()

for _ in range(3):
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.penup()
    t.forward(side - overlap)  # сдвигаемся вправо с заходом
    t.right(90)
    t.forward(side - overlap)  # сдвигаемся вниз с заходом
    t.left(90)
    t.pendown()


# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_free1_1{num}.ps"
filename_png = f"screenshot_free1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

