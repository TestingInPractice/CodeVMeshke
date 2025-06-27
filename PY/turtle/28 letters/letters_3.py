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
t.speed(speed=3)  # Установка скорости анимации (1 - самая медленная)
# Решение Буква Г

t.penup()
t.goto(50, 150)
t.pendown()


t.right(90)
t.forward(100)
t.left(90)
t.forward(40)
t.left(90)
t.forward(100)
t.penup()
t.backward(100)
t.pendown()
t.right(90)
t.forward(40)
t.left(90)
t.forward(100)



# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_letters_{num}.ps"
filename_png = f"screenshot_letters_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

