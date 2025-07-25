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


#https://stepik.org/lesson/1825367/step/3 5.36 Цикл while
# Решение. Нарисовать лестницу из семи ступенек с помощью цикла while
#/CodeVMeshke/PY/turtle/36 while/while_4.py

step = 0
while step < 7:
    t.left(90)       # поднимаемся вверх (вертикальная часть)
    t.forward(40)
    t.right(90)      # поворот в обратную сторону (например, вправо)
    t.forward(40)    # горизонтальная часть ступеньки
    step += 1


# переменная с номером задачи
num=4
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_while_{num}.ps"
filename_png = f"screenshot_while_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

