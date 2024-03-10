from PIL import Image, ImageDraw, ImageFont


def text_to_image(text, output_path='output_image.png', font_size=20, image_size=(300, 200), text_position=(10, 10),
                  text_color=(0, 0, 0), background_color=(255, 255, 255)):
    # Create a blank image with a white background
    image = Image.new('RGB', image_size, background_color)

    # Choose a font and size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the text on the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the image
    image.save(output_path)


if __name__ == "__main__":
    # Example usage
    text_to_image("hello welcome to kasba hood!", output_path='example_image.png')
