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
# Решение Переместить черепашку в точку (100, 100).
# Повернуть черепашку направо на 90 градусов.
# Использовать команды, чтобы узнать и вывести в консоль:
# текущие координаты X и Y,
# текущий угол направления,
# расстояние от текущей позиции до начала координат (0, 0).
t.forward(150)
print("Текущая позиция:", t.position())

# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_st{num}.ps"
filename_png = f"screenshot_st{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

