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

# Гипербола k = 100, правая ветвь (x > 0)
t.color("red")
t.penup()
x = 1
step = 1
scale = 10
while x <= 50:
    y = 100 / x
    t.goto(x * scale, y * scale)
    if x == 1:
        t.pendown()
    x += step
t.penup()

# Гипербола k = 100, левая ветвь (x < 0)
x = -1
while x >= -50:
    y = 100 / x
    t.goto(x * scale, y * scale)
    if x == -1:
        t.pendown()
    x -= step
t.penup()
# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_graf_func_{num}.ps"
filename_png = f"screenshot_graf_func_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

