import turtle
from datetime import datetime

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

#https://stepik.org/lesson/1744608/step/3  5.29 Ввод переменных
# Решение теория Вывод данных в Python и в модуле turtle
#/CodeVMeshke/PY/turtle/31 variables/variables_3.py


txt = input("Введите текст для вывода: ")
t.penup()
t.goto(50,50)
t.write(txt, move=True, align="center", font=("Arial", 16, "normal"))
t.goto(50,30)
a = int(input("Введите число: "))
t.write(a, move=True, align="right", font=("Arial", 20, "bold"))




# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_var_{num}.ps"
filename_png = f"screenshot_var_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

