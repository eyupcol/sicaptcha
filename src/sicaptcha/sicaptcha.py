from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import uuid
import base64

captchaSettings = {
    'bgcolor': (255, 255, 255, 255),
    'textcolor': (0, 0, 0, 250),
    'linecolor': (0, 0, 0, 90),
    'font': 'CaniSketch-Regular.ttf',
    'fontSize': 48,
    'format':'base64', #options: base64|image|buffer
    'imagepath':'captcha.webp',
    'text':'',
}

def get_captcha(captchaSettings):
    textFont = ImageFont.truetype(captchaSettings['font'], captchaSettings['fontSize'])
    background = Image.new("RGBA", (180, 60), captchaSettings['bgcolor'])
    w, h = background.size
    draw = ImageDraw.Draw(background)

    points = []
    for i in range(10):
        points.append((random.randrange(165) + 10, random.randrange(45) + 10));

    draw.line(points, width=5, fill=captchaSettings['linecolor'], joint="curve")

    step = 10
    for x in range(step, w, step):
        for y in range(step, h, step):
            draw.point((x, y), fill=captchaSettings['textcolor'])

    uidStr = str(uuid.uuid4()).split('-')
    captchaSettings['text'] = uidStr[1]
    draw1 = ImageDraw.Draw(background)
    textwidth, textheight = draw1.textsize(captchaSettings['text'], textFont)
    tx = (180 - textwidth) / 2
    ty = (60 - textheight) / 2
    draw1.text((int(tx), int(ty)), captchaSettings['text'], font=textFont, fill=captchaSettings['textcolor'])

    if captchaSettings['format'] == 'base64':
        buffered = BytesIO()
        background.save(buffered, format="WEBP")
        img_str = base64.b64encode(buffered.getvalue())
        return img_str.decode('utf-8')
    elif captchaSettings['format'] == 'image':
        background.save(captchaSettings['imagepath'],'WEBP')
    elif captchaSettings['format'] == 'buffer':
        buffered = BytesIO()
        background.save(buffered, format="WEBP")
        return buffered.getvalue()
    else:
        pass