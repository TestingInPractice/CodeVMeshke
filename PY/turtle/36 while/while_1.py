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


#https://stepik.org/lesson/1825367/step/1 5.36 Цикл while
# Решение. Пример 1: Счётчик с while
# Рассмотрим цикл, который рисует блок из трёх окружностей разного цвета четыре раза:
#/CodeVMeshke/PY/turtle/36 while/while_1.py

colors = ["red", "green", "cyan"]
i = 0
while i < 4:
    for color in colors:
        t.pencolor(color)
        t.circle(30)
        t.penup()
        t.forward(70)
        t.pendown()
    t.penup()
    t.goto(0, (i+1)*70)
    t.pendown()
    i += 1






# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_while_{num}.ps"
filename_png = f"screenshot_while_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

