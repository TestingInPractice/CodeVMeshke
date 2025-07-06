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

# https://stepik.org/lesson/1747822/step/1 5.23 Задания черепашка Цифры
# Решение Нарисовать цифру «1» в стиле российского почтового индекса высотой 100 единиц, вписанную в квадрат 50×50.

#/CodeVMeshke/PY/turtle/23 numbers/num1.py
t.penup()
t.goto(0, 50)
t.pendown()

t.left(45)         # Повернуть налево на 135°, чтобы идти по диагонали вверх-вправо
t.forward(70.7)     # Длина диагонали квадрата 50x50: sqrt(50^2 + 50^2) ≈ 70.7

t.right(135)        # Повернуть направо на 135°, чтобы смотреть вниз
t.forward(100)      # Вертикальная линия вниз (высота цифры)




# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_num_r{num}.ps"
filename_png = f"screenshot_num_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)