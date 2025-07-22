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

#https://stepik.org/lesson/1744603/step/2 5.39 функции def
# Нарисовать Пример функции с параметром
# /CodeVMeshke/PY/turtle/39 def 1/def_1_4.py

def line_without_moving(length):
    t.forward(length)
    t.backward(length)

len=20
# Вызов функции с разными аргументами
t.left(25)
line_without_moving(len)
t.left(25)
line_without_moving(50)
t.left(25)
line_without_moving(80)





# переменная с номером задачи
num=4
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

