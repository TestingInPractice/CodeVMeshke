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
# https://stepik.org/lesson/1707358/step/1 5.12 Внешний вид
# Решение Пример: Управление внешним видом черепахи
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(1)

# 1. Установить форму черепахи (например, "turtle")
t.shape("turtle")

# 2. Включить пользовательский режим изменения размера
t.resizemode("user")

# 3. Изменить размер черепахи: сделать её шире, длиннее и увеличить толщину контура
t.shapesize(stretch_wid=2, stretch_len=3, outline=4)

# 4. Применить сдвиг формы (shearfactor)
t.shearfactor(0.5)

# 5. Установить абсолютный угол наклона формы
t.settiltangle(45)

# 6. Повернуть форму дополнительно на 30 градусов
t.tilt(30)

# 7. Получить и вывести текущий угол наклона формы
angle = t.tiltangle()
t.penup()
t.goto(-150, -100)
t.write(f"Угол наклона формы: {angle}", font=("Arial", 12, "normal"))

# 8. Получить и вывести текущую матрицу преобразования формы
matrix = t.shapetransform()
t.goto(-150, -130)
t.write(f"Матрица преобразования: {matrix}", font=("Arial", 12, "normal"))

# 9. Получить и вывести координаты многоугольника формы
poly = t.get_shapepoly()
t.goto(-150, -160)
t.write(f"Многоугольник формы: {poly[:3]} ...", font=("Arial", 12, "normal"))  # выводим первые 3 точки

# 10. Нарисовать черепаху в новом виде и переместиться
t.goto(100, 100)
t.pendown()
t.forward(100)


# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_appearance{num}.ps"
filename_png = f"screenshot_appearance{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

