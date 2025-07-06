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
# https://stepik.org/lesson/1696637/step/2  5.6 Сказать состояние черепахе + Настройка и измерение

# Решение  Задание 2: Переместить черепашку в точку (100, 100).
# Повернуть черепашку направо на 90 градусов.
# Использовать команды, чтобы узнать и вывести в консоль:
# текущие координаты X и Y,
# текущий угол направления,
# расстояние от текущей позиции до начала координат (0, 0).
t.goto(100, 100)
t.right(90)
print("Координата X:", t.xcor())
print("Координата Y:", t.ycor())
print("Угол направления:", t.heading())
print("Расстояние до (0,0):", t.distance(0, 0))

# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_st{num}.ps"
filename_png = f"screenshot_st{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

