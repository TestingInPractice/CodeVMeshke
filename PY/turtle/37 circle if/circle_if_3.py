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
# Решение
#https://stepik.org/lesson/1744604/step/1 5.37 Цикл с условием
# Оператор if-elif-else
# Позволяет проверить несколько условий последовательно.
#/CodeVMeshke/PY/turtle/37 circle if/circle_if_3.py

u = input("Хотите, чтобы я нарисовал фигуру? Введите y или n: ")
if u == "y":
    t.circle(50)
elif u == "n":
    print("Хорошо, не рисуем")
else:
    print("Неверный ввод")


# переменная с номером задачи
num=3
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

