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

#https://stepik.org/lesson/1757671/step/3 5.34 Цикл 3 Задания
# Решение. Рисует правильный пятиугольник со стороной 100.
#/CodeVMeshke/PY/turtle/34 circle 3/circle3_3.py



side_length = 100
angle = 72  # угол поворота для пятиугольника (360° / 5)

for _ in range(5):
    t.forward(side_length)
    t.left(angle)


# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle{num}.ps"
filename_png = f"screenshot_circle{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

