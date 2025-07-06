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

# https://stepik.org/lesson/1757670/step/7 5.24 Задания черепашка 2 простые фигуры
# Решение Напишите программу, которая с помощью черепашки нарисует фигуру из двух перевернутых треугольников. Основание верхнего треугольника Y = 100.


#/CodeVMeshke/PY/turtle/24 simple fig 2/sf_r7.py
t.left(135)         # 1. Повернуть вверх-влево
t.forward(140)      # 2. Диагональ

t.right(135)        # 3. Повернуть вправо
t.forward(100)      # 4. Верхняя сторона прямоугольника

t.right(90)         # 5. Повернуть вниз
t.forward(100)      # 6. Правая сторона прямоугольника

t.right(90)         # 7. Повернуть влево
t.forward(100)      # 8. Нижняя сторона прямоугольника

t.left(135)         # 9. Повернуть вниз-влево
t.forward(140)      # 10. Нижняя диагональ

# переменная с номером задачи
num=7
# Получаем холст tkinter
canvas = turtle.getcanvas()
# Сохраняем содержимое холста в файл postscript
filename_ps = f"screenshot_sf_r{num}.ps"
filename_png = f"screenshot_sf_r{num}.png"
# Сохраняем содержимое холста в файл postscript
canvas.postscript(file=filename_ps, colormode='color')
# Конвертируем postscript в PNG
img = Image.open(filename_ps)
img.save(filename_png)
# Удаляем временный файл
os.remove(filename_ps)
turtle.done()  #(окно не закрывается сразу)

