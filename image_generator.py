from PIL import ImageFont, ImageDraw, Image
import time

font_name = "Aller_Bd.ttf"


async def generate_osu_image(text, req_id):
    text = text.upper()
    image = Image.open('osu_base.png')
    draw = ImageDraw.Draw(image)
    font_size = 1  # starting font size

    img_fraction = 0.75
    img_frac_height = 0.45

    img_width = image.size[0]
    img_height = image.size[1]

    font = ImageFont.truetype(font_name, font_size)

    while font.getsize(text)[0] < img_fraction * img_width:
        font_size += 1
        font = ImageFont.truetype(font_name, font_size)

    while font.getsize(text)[1] > img_frac_height * img_height:
        font_size -= 1
        font = ImageFont.truetype(font_name, font_size)

    font_size -= 1
    font = ImageFont.truetype(font_name, font_size)

    text_width = font.getsize(text)[0]
    text_height = font.getsize(text)[1]

    draw.text(((img_width - text_width) / 2, (img_height - text_height) / 2), text, font=font)

    image_path = 'tmp/{}-{}.png'.format(req_id, time.time())
    image.save(image_path)
    return image_path
