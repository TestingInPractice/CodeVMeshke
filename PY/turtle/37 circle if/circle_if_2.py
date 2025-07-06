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

#https://stepik.org/lesson/1744604/step/1 5.37 Цикл с условием
# Решение.Оператор if-else
# Позволяет задать альтернативное действие, если условие ложно.
#/CodeVMeshke/PY/turtle/37 circle if/circle_if_2.py


u = input("Хотите, чтобы я нарисовал фигуру? Введите y или n: ")
if u == "y":
    t.circle(50)
else:
    print("Хорошо, ничего не рисуем")
# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_if_{num}.ps"
filename_png = f"screenshot_circle_if_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

