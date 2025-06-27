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

#Нарисовать три соединённых шестиугольника разного цвета

def draw_hexagon(length, color):
    t.pencolor(color)
    for _ in range(6):
        t.forward(length)
        t.left(60)

side = 80

# Первый (верхний) шестиугольник — синий
draw_hexagon(side, "blue")

# Перейти к позиции для второго (среднего) шестиугольника
t.penup()
t.forward(side)
t.right(60)
t.pendown()
draw_hexagon(side, "red")

# Перейти к позиции для третьего (нижнего) шестиугольника
t.right(120)
draw_hexagon(side, "green")






# переменная с номером задачи
num=9
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_def_1_{num}.ps"
filename_png = f"screenshot_def_1_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

