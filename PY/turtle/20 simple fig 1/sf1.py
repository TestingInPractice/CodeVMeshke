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
# Решение Задание: Нарисуйте наклонные параллельные линии. Линии начинаются в точках с Y = 0, -50 и -100 и идут под одинаковым наклоном.

t.left(45)
t.forward(100)

t.penup()
t.goto(0, -50)
t.pendown()
t.left(0)  # угол уже повернут, можно не менять
t.forward(100)

t.penup()
t.goto(0, -100)
t.pendown()
t.left(0)
t.forward(100)



# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf1_r{num}.ps"
filename_png = f"screenshot_sf1_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)