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
t.speed(speed=3)  # Установка скорости анимации (1 - самая медленная)

# https://stepik.org/lesson/1809578/step/1 5.28 Задания черепашки Буквы
# Решение Буква П

#/CodeVMeshke/PY/turtle/28 letters/letters_1.py
t.penup()
t.goto(50, 50)
t.pendown()

# Повернуть вверх
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_letters_{num}.ps"
filename_png = f"screenshot_letters_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

