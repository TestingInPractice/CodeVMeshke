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

#https://stepik.org/lesson/1744603/step/1 5.39 функции def
# Нарисовать # Корень y = sqrt(x), x >= 0
# /CodeVMeshke/PY/turtle/40 def 1/def_1_1.py




def draw_three_lines():
    for _ in range(3):
        t.right(20)
        t.forward(50)
        t.penup()
        t.backward(50)
        t.right(100)
        t.pendown()

draw_three_lines()




# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_1_{num}.ps"
filename_png = f"screenshot_def_1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

