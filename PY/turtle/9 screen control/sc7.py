import turtle
from PIL import Image
import os
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

#https://stepik.org/lesson/1727576/step/1 5.16 Общественные классы
screen = turtle.Screen()
t = turtle.Turtle()



# Создаём экран (объект Screen - подкласс TurtleScreen)
screen = turtle.Screen()
screen.title("Пример классов turtle")

# Создаём черепаху (объект Turtle - подкласс RawTurtle)
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.speed(3)

# Используем класс Vec2D для задания вектора перемещения
from turtle import Vec2D
move_vector = Vec2D(100, 50)

# Перемещаем черепаху с помощью вектора
t1.penup()
t1.goto(move_vector)
t1.pendown()

# Рисуем квадрат
for _ in range(4):
    t1.forward(50)
    t1.right(90)

# Создаём вторую черепаху, чтобы показать работу с несколькими объектами
t2 = turtle.Turtle()
t2.shape("circle")
t2.color("red")
t2.speed(5)
t2.penup()
t2.goto(-100, -100)
t2.pendown()

# Рисуем треугольник
for _ in range(3):
    t2.forward(80)
    t2.left(120)

# Демонстрация использования класса Shape для регистрации новой формы
pentagon_points = ((0,0), (20,60), (60,80), (100,60), (120,0))
pentagon_shape = turtle.Shape("polygon", pentagon_points)
screen.register_shape("pentagon", pentagon_shape)

t1.shape("pentagon")
t1.penup()
t1.goto(0, 100)
t1.pendown()
t1.stamp()  # Отпечаток новой формы

# Вывести список всех черепах на экране
print("Черепахи на экране:", screen.turtles())






# переменная с номером задачи
num=7
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sс{num}.ps"
filename_png = f"screenshot_sс{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)