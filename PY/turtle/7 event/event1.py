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
# https://stepik.org/lesson/1707359/step/1 5.13 Использование событий
# Решение
# Установить цвет пера красный и цвет заливки жёлтый
t.pencolor("red")
t.fillcolor("yellow")

# Сбросить всё и начать с чистого листа
t.reset()
t.speed(1)

# Привязка функций к событиям

# Функция для обработки щелчка мыши
def on_click(x, y):
    print(f"Щелчок в координатах: ({x}, {y})")

# Функция для обработки отпускания кнопки мыши
def on_release(x, y):
    print("Кнопка отпущена!")

# Функция для обработки перетаскивания мыши
def on_drag(x, y):
    t.ondrag(None)  # временно отключаем обработчик, чтобы избежать рекурсии
    t.goto(x, y)
    t.ondrag(on_drag)

# Настройка черепахи
t.shape("turtle")
t.pendown()

# Привязка функций к событиям
t.onclick(on_click)
t.onrelease(on_release)
t.ondrag(on_drag)

turtle.done()



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

