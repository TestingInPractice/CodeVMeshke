
import turtle

# 1. Создать окно и изменить цвет фона
screen = turtle.Screen()
screen.bgcolor("orange")
print("Цвет фона:", screen.bgcolor())

# 2. Установить фоновое изображение, затем удалить его
# (Убедитесь, что файл landscape.gif есть в папке)
try:
    screen.bgpic("auto_grid.gif")
    print("Фоновое изображение:", screen.bgpic())
except turtle.TurtleGraphicsError:
    print("Файл landscape.gif не найден, пропускаем установку фонового изображения.")
screen.bgpic("nopic")
print("Фоновое изображение после удаления:", screen.bgpic())

# 3. Нарисовать линию и очистить только рисунок
t = turtle.Turtle()
t.forward(100)
t.clear()  # Очищает рисунок, черепаха остаётся на месте

# 4. Нарисовать новую линию и сбросить черепаху
t.forward(50)
t.reset()  # Сброс черепахи в исходное состояние

# 5. Изменить размер холста и проверить его
print("Размер холста до изменения:", screen.screensize())
screen.screensize(1200, 800)
print("Размер холста после изменения:", screen.screensize())

# 6. Установить пользовательскую систему координат и нарисовать прямоугольник
screen.setworldcoordinates(-400, -300, 400, 300)
t.penup()
t.goto(-400, -300)
t.pendown()
for _ in range(2):
    t.forward(800)
    t.left(90)
    t.forward(600)
    t.left(90)

turtle.done()
