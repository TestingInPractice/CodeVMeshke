import turtle
# Двигаться и рисовать https://stepik.org/lesson/1696636/step/6
# Задание 8: Переместить черепашку в координаты 50:50 и вернуться в 0:0
# Настройки окна
turtle.setup(800, 600)
turtle.bgpic("auto_grid.gif")  # Укажите правильный путь к файлу!
turtle.title("Черепашка на координатной сетке")
# Настройки черепашки
t = turtle.Turtle()
t.shape("turtle")
# Пример движения
t.goto(50,50)
t.home()
turtle.done()