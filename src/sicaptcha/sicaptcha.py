from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import uuid
import base64
import os


class Sicaptcha:
    bgcolor = (255, 255, 255, 255)
    textcolor = (0, 0, 0, 250)
    linecolor = (0, 0, 0, 90)
    font = ""
    fontSize = 48
    format = 'base64' #options: base64|image|buffer
    imagepath = 'captcha.webp'
    text = ''

    def get_captcha(self):
        if not os.path.isfile(self.font) or self.font == "":
            textFont = ImageFont.load_default()
        else:
            textFont = ImageFont.truetype(self.font, self.fontSize)

        background = Image.new("RGBA", (180, 60), self.bgcolor)
        w, h = background.size
        draw = ImageDraw.Draw(background)

        points = []
        for i in range(10):
            points.append((random.randrange(165) + 10, random.randrange(45) + 10));

        draw.line(points, width=5, fill=self.linecolor, joint="curve")

        step = 10
        for x in range(step, w, step):
            for y in range(step, h, step):
                draw.point((x, y), fill=self.textcolor)

        uidStr = str(uuid.uuid4()).split('-')

        draw1 = ImageDraw.Draw(background)
        textwidth, textheight = draw1.textsize(uidStr[1], textFont)
        tx = (180 - textwidth) / 2
        ty = (60 - textheight) / 2
        draw1.text((int(tx), int(ty)), uidStr[1], font=textFont, fill=self.textcolor)

        if self.format == 'base64':
            buffered = BytesIO()
            background.save(buffered, format="WEBP")
            img_str = base64.b64encode(buffered.getvalue())
            return img_str
        elif self.format == 'image':
            background.save(self.imagepath, 'WEBP')
        else:
            buffered = BytesIO()
            background.save(buffered, format="WEBP")
            return buffered.getvalue()