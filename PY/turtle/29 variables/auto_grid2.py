from PIL import Image, ImageDraw, ImageFont

# Создаем изображение 800x600 пикселей
width, height = 800, 600
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Центр координат (0,0)
center_x, center_y = width // 2, height // 2

# Загрузка шрифта (лучше использовать файл шрифта)
try:
    font = ImageFont.truetype("arial.ttf", 12)
except:
    font = ImageFont.load_default()


# Функция для расчета размера текста
def get_text_size(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


# Рисуем основную сетку (шаг 10 пикселей)
for x in range(0, width, 10):
    draw.line([(x, 0), (x, height)], fill="#F0F0F0")
for y in range(0, height, 10):
    draw.line([(0, y), (width, y)], fill="#F0F0F0")

# Рисуем координатные оси
axis_color = "black"
draw.line([(0, center_y), (width, center_y)], fill=axis_color, width=2)  # Ось X
draw.line([(center_x, 0), (center_x, height)], fill=axis_color, width=2)  # Ось Y

# Рисуем метки и подписи на осях (шаг 50 пикселей)
label_color = "black"
for coord in range(0, width, 50):
    if coord != center_x:
        # Метки на оси X
        draw.line([(coord, center_y - 3), (coord, center_y + 3)], fill=label_color)

        # Подписи каждые 100 пикселей
        if coord % 100 == 0:
            value = (coord - center_x) // 1  # Масштаб 1:1
            text = str(value)
            text_width, text_height = get_text_size(text, font)
            draw.text(
                (coord - text_width // 2, center_y + 10),
                text,
                fill=label_color,
                font=font
            )

for coord in range(0, height, 50):
    if coord != center_y:
        # Метки на оси Y
        draw.line([(center_x - 3, coord), (center_x + 3, coord)], fill=label_color)

        # Подписи каждые 100 пикселей
        if coord % 100 == 0:
            value = (center_y - coord) // 1  # Масштаб 1:1
            text = str(value)
            text_width, text_height = get_text_size(text, font)
            draw.text(
                (center_x - text_width - 15, coord - text_height // 2),
                text,
                fill=label_color,
                font=font
            )

# Подписываем начало координат (0,0)
zero_text = "(0,0)"
zero_width, zero_height = get_text_size(zero_text, font)
draw.text(
    (center_x + 10, center_y + 5),
    zero_text,
    fill="red",
    font=font
)

# Подписываем оси
x_label = "X"
y_label = "Y"
label_offset = 20

# Подпись оси X
x_width, x_height = get_text_size(x_label, font)
draw.text(
    (width - x_width - 10, center_y + 10),
    x_label,
    fill=label_color,
    font=font
)

# Подпись оси Y
y_width, y_height = get_text_size(y_label, font)
draw.text(
    (center_x + 10, 10),
    y_label,
    fill=label_color,
    font=font
)

# Сохраняем изображение
img.save("coordinate_grid.png")
print("Грид с координатами сохранен как coordinate_grid.png")

img.save("auto_grid.gif")