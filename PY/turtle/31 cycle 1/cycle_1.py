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

#https://stepik.org/lesson/1744607/step/1  5.31 Цикл + задания for без условия
# Решение Использование циклов в Python
#/CodeVMeshke/PY/turtle/31 cycle 1/cycle_1.py


# for i in range(5):
#     print(i)
# # Выведет:
# # 0
# # 1
# # 2
# # 3
# # 4
#
# for char in "Python":
#     print(char)
# # Выведет:
# # P
# # y
# # t
# # h
# # o
# # n
#
# colors = ["red", "green", "blue"]
# for color in colors:
#     print("Цвет:", color)
#
#
# n = 1
# while n <= 10:
#     print(n)
#     n += 1

#Таблица умножения
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)
    print("---")


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cycle_{num}.ps"
filename_png = f"screenshot_cycle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

