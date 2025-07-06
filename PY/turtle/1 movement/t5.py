import turtle
# Двигаться и рисовать https://stepik.org/lesson/1696636/step/5
# Задание 7 Повернуть черепашку на 90 градусов влево
# Настройки окна
turtle.setup(800, 600)
turtle.bgpic("auto_grid.gif")  # Укажите правильный путь к файлу!
turtle.title("Черепашка на координатной сетке")
# Настройки черепашки
t = turtle.Turtle()
t.shape("turtle")
# Пример движения
t.left(90)
turtle.done()