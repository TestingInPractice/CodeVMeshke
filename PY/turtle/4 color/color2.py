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
# https://stepik.org/lesson/1707356/step/4 5.10 Управление цветом+Заполнение+Больше контроля рисования
# Решение Задание 2: Очистка экрана и вывод текста
# Нарисовать квадрат со стороной 100.
# Использовать функцию write(), чтобы вывести под квадратом текст:
# сначала написать "Квадрат нарисован" по центру,
# затем вывести координаты текущей позиции черепашки рядом с текстом.
# Использовать функцию clear(), чтобы стереть рисунок, но оставить текст и положение черепашки.
# Нарисовать круг радиусом 50.
# Использовать функцию reset(), чтобы очистить всё и вернуть черепашку в центр с настройками по умолчанию.

t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# Вывести текст под квадратом
t.penup()
t.goto(50, -20)
t.write("Квадрат нарисован", align="center", font=("Arial", 12, "normal"))
t.write(t.pos(), True)

# Очистить рисунок, но не текст и положение черепашки
t.clear()

# Нарисовать круг
t.pendown()
t.circle(50)

# Сбросить всё и вернуть черепашку в центр
t.reset()

# переменная с номером задачи
num=2
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_color{num}.ps"
filename_png = f"screenshot_color{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

