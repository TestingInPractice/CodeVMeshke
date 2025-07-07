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
#https://stepik.org/lesson/1769319/step/2 5.42 Продвинутое использование переменных 1
# Напишите программу для рисования расширения кругов. Ваша программа должна:
# Использовать процедуру, которая рисует круг с центром в точке (x, y) и радиусом radius.
# На каждом шаге цикла рисовать круг с радиусом, уменьшающимся на 1 пиксель.
# /CodeVMeshke/PY/turtle/43 prod var/prod_var_2.py

def draw_tunnel_circles(x, y, start_radius, count):
    """
    Рисует тоннель из кругов с центром в (x, y).
    start_radius — радиус самого маленького круга,
    count — количество кругов.
    Каждый следующий круг рисуется с радиусом на 1 меньше предыдущего.
    """
    radius = start_radius
    for _ in range(count):
        t.penup()
        t.goto(x, y - radius)  # смещаем вниз на radius, чтобы центр круга был в (x, y)
        t.pendown()
        t.circle(radius)
        radius -= 1

# Пример вызова:
draw_tunnel_circles(0, 0, 100, 40)





# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_prod_var_{num}.ps"
filename_png = f"screenshot_prod_var_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

