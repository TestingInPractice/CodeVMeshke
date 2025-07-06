import turtle
from PIL import Image
import os

# https://stepik.org/lesson/1727575/step/2 5.15 TurtleScreen Контроль за окном+

# Пример: 
# Нарисуйте 50 квадратов, каждый следующий - чуть больше предыдущего, с анимацией по умолчанию.
# Очистите экран, затем выключите анимацию (tracer(0)), нарисуйте ещё 50 квадратов (разного размера), после чего вручную обновите экран с помощью update().
# Измените задержку отрисовки с помощью delay() и нарисуйте 10 квадратов, чтобы увидеть разницу в скорости.
# Измените скорость черепахи методом speed() и нарисуйте 10 квадратов для сравнения.


screen = turtle.Screen()
t = turtle.Turtle()

# 1. Анимация по умолчанию
for i in range(50, 100, 1):
    for _ in range(4):
        t.forward(i)
        t.left(90)
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()

t.clear()

# 2. Отключаем анимацию и обновляем экран вручную
screen.tracer(0)  # Отключаем автоматическую анимацию
for i in range(50, 100, 1):
    for _ in range(4):
        t.forward(i)
        t.left(90)
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()
screen.update()   # Показываем результат сразу

t.clear()
screen.tracer(1)  # Включаем анимацию обратно

# 3. Меняем задержку отрисовки
screen.delay(200)  # 200 миллисекунд между обновлениями
for i in range(10):
    for _ in range(4):
        t.forward(50 + i*10)
        t.left(90)
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()

t.clear()
screen.delay(10)  # Возвращаем задержку по умолчанию

# 4. Меняем скорость черепахи
t.speed(1)  # Самая медленная
for i in range(10):
    for _ in range(4):
        t.forward(30 + i*5)
        t.left(90)
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()

t.speed(10)  # Самая быстрая
for i in range(10):
    for _ in range(4):
        t.forward(30 + i*5)
        t.left(90)
    t.penup()
    t.right(10)
    t.forward(10)
    t.pendown()

# переменная с номером задачи
num=2
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