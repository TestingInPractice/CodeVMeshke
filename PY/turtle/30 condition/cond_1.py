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

#https://stepik.org/lesson/1744609/step/1  5.30 Условия If
# Решение Работа с вводом и условием — пример для черепахи
#/CodeVMeshke/PY/turtle/30 condition/cond_1.py

direction = input("Идти налево или направо? ").strip().lower()
if direction == "left":
    t.left(60)
    t.forward(50)
elif direction == "right":
    t.right(60)
    t.forward(50)
else:
    print("Неверная команда. Введите 'left' или 'right'.")


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_cond_{num}.ps"
filename_png = f"screenshot_cond_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

