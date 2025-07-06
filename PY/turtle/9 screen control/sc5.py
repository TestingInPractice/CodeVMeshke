import turtle
from PIL import Image
import os
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

# https://stepik.org/lesson/1727575/step/5 5.15 TurtleScreen Контроль за окном+

screen = turtle.Screen()
t = turtle.Turtle()

# 1. Определить и вывести текущий режим
print("Текущий режим:", screen.mode())

# 2. Установить режим "logo" и нарисовать стрелку вверх
screen.mode("logo")
t.setheading(0)
t.forward(100)
t.penup()
t.goto(0, 0)
t.pendown()

# 3. Сменить цветовой режим на 255 и нарисовать круг с цветом (128, 0, 255)
screen.colormode(255)
t.color((128, 0, 255))
t.circle(50)

# 4. Получить и вывести список всех форм черепахи
print("Доступные формы:", screen.getshapes())

# 5. Зарегистрировать новую форму - пятиугольник
# Создаем объект Shape типа "polygon"
pentagon = turtle.Shape("polygon", [(0,0), (20,60), (60,80), (100,60), (120,0)])

# Регистрируем форму
screen.register_shape("pentagon", pentagon)

# Используем форму
t.shape("pentagon")
t.stamp()

# 6. Получить объект холста и вывести его тип
canvas = screen.getcanvas()
print("Тип холста:", type(canvas))

# 7. Создать двух черепах и вывести список всех черепах
t2 = turtle.Turtle()
t3 = turtle.Turtle()
print("Все черепахи:", screen.turtles())

# 8. Получить и вывести размеры окна
print("Размеры окна:", screen.window_width(), "x", screen.window_height())






# переменная с номером задачи
num=5
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