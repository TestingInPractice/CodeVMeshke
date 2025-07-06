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

# https://stepik.org/lesson/1757670/step/1 5.24 Задания черепашка 2 простые фигуры
# Решение Нарисовать правильную восьмиконечную звезду.
# Черепашка должна нарисовать правильную восьмиконечную звезду, где каждая сторона равна 100 единицам.
# Используйте команды:
# t.forward(distance), t.right(angle)
# Подсказка: Для восьмиконечной звезды угол поворота равен 135° (внешний угол).

#/CodeVMeshke/PY/turtle/24 simple fig 2/sf_r1.py
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)
t.forward(100)
t.right(135)


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf_r{num}.ps"
filename_png = f"screenshot_sf_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

