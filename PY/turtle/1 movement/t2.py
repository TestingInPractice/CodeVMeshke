import turtle


def draw_grid(step=50, color="gray"):
    """Рисует координатную сетку с заданным шагом"""
    t = turtle.Turtle()
    t.speed(0)  # Максимальная скорость
    t.hideturtle()
    t.color(color)

    # Получаем размеры окна
    width = turtle.window_width()
    height = turtle.window_height()

    # Вертикальные линии
    for x in range(-width // 2, width // 2, step):
        t.penup()
        t.goto(x, -height // 2)
        t.pendown()
        t.goto(x, height // 2)

    # Горизонтальные линии
    for y in range(-height // 2, height // 2, step):
        t.penup()
        t.goto(-width // 2, y)
        t.pendown()
        t.goto(width // 2, y)


# Настройки окна
turtle.setup(800, 600)  # Размер окна
turtle.bgcolor("white")  # Цвет фона
draw_grid(step=50)  # Рисуем сетку с шагом 50px

# Настраиваем черепашку
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.shapesize(2)

# Пример движения
# t.forward(100)
# t.left(90)
# t.forward(100)

turtle.done()