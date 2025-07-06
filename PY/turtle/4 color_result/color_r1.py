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
# https://stepik.org/lesson/1707356/step/5 5.10 Управление цветом+Заполнение+Больше контроля рисования
# Решение Задание: Установить цвет пера синий, цвет заливки жёлтый.
# Нарисовать заполненный круг диаметром 100. Использовать color+begin_fill+circle+end_fill
t.color("blue", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
# переменная с номером задачи
num=1
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_color_r{num}.ps"
filename_png = f"screenshot_color_r_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

