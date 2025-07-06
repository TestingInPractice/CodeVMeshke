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

#https://stepik.org/lesson/1744608/step/2  5.29 Ввод переменных
# Решение Упражнение: Домик — практическое задание
# /CodeVMeshke/PY/turtle/31 variables/variables_2.py


# Длина стороны квадрата (основания дома)
side = 100
# Рисуем квадрат - основание дома
t.forward(side)
t.left(90)
t.forward(side)
t.left(90)
t.forward(side)
t.left(90)
t.forward(side)
t.goto(0,100)
t.left(150)

#крыша
t.forward(side)
t.right(120)
t.forward(side)





# переменная с номером задачи
num=2
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

