import turtle

# Настройки окна
turtle.setup(800, 600)
turtle.bgpic("auto_grid.gif")  # Укажите правильный путь к файлу!
turtle.title("Черепашка на координатной сетке")

# Настройки черепашки
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.shapesize(2)

# Пример движения
t.forward(100)
t.left(90)
t.forward(100)

turtle.done()