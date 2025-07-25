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
# https://stepik.org/lesson/1707356/step/1 5.11 Состояние черепахи Видимость
# Решение Задание: Управление видимостью черепахи
# Нарисовать круг диаметром 50, предварительно скрыв черепаху (чтобы ускорить рисование и не показывать саму черепашку). После завершения рисунка снова показать черепаху.
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Нарисовать круг с заливкой
# Скрыть черепаху перед рисованием
t.hideturtle()
t.circle(50)
t.home()

# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_turt_state{num}.ps"
filename_png = f"screenshot_turt_state{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

