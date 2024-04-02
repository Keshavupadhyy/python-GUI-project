from PIL import Image, ImageDraw, ImageFont
import random


class MemeGenerator:
    def __init__(self, image_path, top_text, bottom_text, font_path="arial.ttf", font_size=20):
        self.image_path = image_path
        self.top_text = top_text
        self.bottom_text = bottom_text
        self.font_path = font_path
        self.font_size = font_size
        self.font = ImageFont.truetype(font_path, font_size)
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
        self.image_width, self.image_height = self.image.size

    def add_text(self, text, position="center"):
        text_width, text_height = self.draw.textsize(text, font=self.font)
        if position == "center":
            x = (self.image_width - text_width) / 2
        elif position == "bottom":
            x = (self.image_width - text_width) / 2
        else:
            x = 10
        if position == "top":
            y = 10
        elif position == "bottom":
            y = self.image_height - text_height - 10
        else:
            y = (self.image_height - text_height) / 2
        self.draw.text((x, y), text, font=self.font, fill="white")

    def add_outline(self, text, position="center", outline_color="black", outline_width=2):
        for offset in range(1, outline_width + 1):
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            self.add_text(text, position)
            if position == "center":
                x = (self.image_width - offset) / 2
            elif position == "bottom":
                x = (self.image_width - offset) / 2
            else:
                x = 10 - offset
            if position == "top":
                y = 10 - offset
            elif position == "bottom":
                y = self.image_height - self.font_size - 10 - offset
            else:
                y = (self.image_height - self.font_size) / 2 - offset
            self.draw.text((x, y), text, font=self.font, fill=outline_color)

    def generate_meme(self, outfile="meme_generated.png"):
        self.add_outline(self.top_text, "top")
        self.add_outline(self.bottom_text, "bottom")
        self.image.save(outfile)


# Example usage
image_path = "Lionel-Messi-Argentina-2022-FIFA-World-Cup_(cropped).jpg"
top_text = "Ronaldo mere"
bottom_text = "Lund sae"
font_path = "impact.ttf"  # You can choose a different font
font_size = 40

meme_generator = MemeGenerator(image_path, top_text, bottom_text, font_path, font_size)
meme_generator.generate_meme("meme_generated_advanced.png")
