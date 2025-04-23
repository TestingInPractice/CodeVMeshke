from PIL import Image, ImageDraw

# Создаем изображение 800x600
img = Image.new("RGB", (800, 600), "white")
draw = ImageDraw.Draw(img)

# Рисуем сетку (шаг 10 пикселей)
for x in range(0, 800, 10):
    draw.line([(x, 0), (x, 600)], fill="lightgray")
for y in range(0, 600, 10):
    draw.line([(0, y), (800, y)], fill="lightgray")

# Сохраняем
img.save("auto_grid.gif")

# Теперь можно использовать turtle.bgpic("auto_grid.gif")