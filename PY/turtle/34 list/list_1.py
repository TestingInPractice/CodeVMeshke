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
t.speed(speed=4)  # Установка скорости анимации (1 - самая медленная)
# Решение ​
# Нарисовать из центра 5 кругов разного размера и цвета в цикле, используя список цветов 
#
# colors = ['', 'purple', 'orange', 'cyan', 'magenta', 'lime']
#
# На каждом шаге цикла менять цвет круга и увеличивать радиус.
#
# ​

colors = ['', 'purple', 'orange', 'cyan', 'magenta', 'lime']

circle_radius = 25
radius_increment = 20

t.penup()
t.goto(0, 0)
t.pendown()

for index in range(1, 6):  # пропускаем первый пустой цвет
    t.color(colors[index])
    t.penup()
    t.goto(0, -circle_radius)  # смещаемся вниз на радиус для правильного центра круга
    t.pendown()
    t.circle(circle_radius)
    circle_radius += radius_increment

# переменная с номером задачи
num=5
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_list_{num}.ps"
filename_png = f"screenshot_list_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

