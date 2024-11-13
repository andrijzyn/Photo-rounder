from PIL import Image, ImageDraw

def round_corners(image_path, output_path, radius):
    # Открываем изображение
    img = Image.open(image_path).convert("RGBA")

    # Создаем маску
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)

    # Рисуем закругленные углы
    draw.rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=radius, fill=255)

    # Применяем маску к изображению
    rounded_img = Image.new('RGBA', img.size)
    rounded_img.paste(img, (0, 0), mask)

    # Сохраняем результат
    rounded_img.save(output_path, format="PNG")

# Пример использования
round_corners("input_image.png", "output_image.png", radius=50)