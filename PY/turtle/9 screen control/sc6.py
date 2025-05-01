import turtle
from PIL import Image
import os
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")



screen = turtle.Screen()
t = turtle.Turtle()


# 1. Настройка окна
screen = turtle.Screen()
screen.setup(width=800, height=600, startx=None, starty=None)  # Центрирование окна
screen.title("Моя черепашья графика")

# 2. Создание черепахи и рисование квадрата
t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)

# 3. Закрытие окна по клику мыши
turtle.exitonclick()




# переменная с номером задачи
num=6
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sс{num}.ps"
filename_png = f"screenshot_sс{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)