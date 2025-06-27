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



def draw_ring(x, y, color, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pencolor(color)
    t.circle(radius)

radius = 25  # Диаметр 50, значит радиус 25
dx = 60      # Горизонтальное расстояние между центрами колец
dy = 30      # Вертикальное смещение для нижнего ряда

# Верхний ряд
draw_ring(0, 0, "blue", radius)
draw_ring(dx, 0, "black", radius)
draw_ring(2*dx, 0, "red", radius)

# Нижний ряд
draw_ring(dx//2, -dy, "yellow", radius)
draw_ring(dx + dx//2, -dy, "green", radius)




# переменная с номером задачи
num=8
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_2_{num}.ps"
filename_png = f"screenshot_def_2_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

