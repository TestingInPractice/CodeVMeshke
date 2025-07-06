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
# https://stepik.org/lesson/1707360/step/1 5.14 Специальные методы Turtle
# Решение Специальные методы черепахи в turtle
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(1)

# Привязка функций к событиям
# 1. Начать запись многоугольника
t.begin_poly()

# 2. Нарисовать треугольник
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 3. Завершить запись и получить координаты
t.end_poly()
poly = t.get_poly()
t.penup()
t.goto(-150, -100)
t.write(f"Вершины треугольника: {poly}", font=("Arial", 10, "normal"))

# 4. Создать клона и нарисовать второй треугольник
clone_turtle = t.clone()
clone_turtle.penup()
clone_turtle.goto(150, 0)
clone_turtle.pendown()

clone_turtle.forward(100)
clone_turtle.left(120)
clone_turtle.forward(100)
clone_turtle.left(120)
clone_turtle.forward(100)
clone_turtle.left(120)

# 5. Получить объекты черепахи и экрана
main_turtle = t.getturtle()
screen = t.getscreen()

# 6. Установить размер буфера отмены
t.setundobuffer(10)

# 7. Нарисовать линию, отменить, вывести количество записей в буфере
t.penup()
t.goto(0, -150)
t.pendown()
t.forward(100)
t.undo()
entries = t.undobufferentries()
t.penup()
t.goto(0, -170)
t.write(f"Осталось в буфере отмены: {entries}", font=("Arial", 10, "normal"))




# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_stt{num}.ps"
filename_png = f"screenshot_stt{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

