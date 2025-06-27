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
t.speed(1)


# Рисуем лицо
t.penup()
t.goto(0, -100)          # Переместиться в нижнюю точку круга
t.pendown()
t.fillcolor("yellow")    # Цвет заливки лица
t.begin_fill()
t.circle(100)            # Круг с радиусом 100
t.end_fill()

# Рисуем левый глаз
t.penup()
t.goto(-40, 30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(15)
t.end_fill()

# Рисуем правый глаз
t.penup()
t.goto(40, 30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(15)
t.end_fill()

# Рисуем рот
t.penup()
t.goto(-40, -20)
t.pendown()
t.pencolor("red")
t.width(5)
t.setheading(-60)
t.circle(50, 120)  # Дуга рот



# переменная с номером задачи
num=3
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_circle_{num}.ps"
filename_png = f"screenshot_circle_{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

