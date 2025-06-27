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
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(3)


colors = ["black", "white"]  # цвета для переключения
current_color = ""           # начальное значение цвета
m = 5                        # количество квадратов
n = 4                        # количество сторон квадрата
length = 40                  # длина стороны квадрата

for step in range(m):
    if current_color == "black":
        current_color = "white"
    else:
        current_color = "black"
    t.fillcolor(current_color)
    t.begin_fill()
    for _ in range(n):
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(length)
    t.pendown()
# переменная с номером задачи
num=5
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

