from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

class MemeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Generator")

        # Create labels, buttons, and entry widgets
        self.top_text_label = tk.Label(root, text="Top Text:")
        self.top_text_entry = tk.Entry(root)

        self.bottom_text_label = tk.Label(root, text="Bottom Text:")
        self.bottom_text_entry = tk.Entry(root)

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.generate_button = tk.Button(root, text="Generate Meme", command=self.generate_meme)

        # Grid layout
        self.top_text_label.grid(row=0, column=0, padx=10, pady=5)
        self.top_text_entry.grid(row=0, column=1, padx=10, pady=5)

        self.bottom_text_label.grid(row=1, column=0, padx=10, pady=5)
        self.bottom_text_entry.grid(row=1, column=1, padx=10, pady=5)

        self.upload_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            print("Image Uploaded:", self.image_path)

    def generate_meme(self):
        if hasattr(self, 'image_path'):
            top_text = self.top_text_entry.get()
            bottom_text = self.bottom_text_entry.get()

            # Open the image
            img = Image.open(self.image_path)
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()

            # Add text to the image
            text_width, text_height = draw.textsize(top_text, font)
            draw.text(((img.width - text_width) / 2, 10), top_text, (255, 255, 255), font=font)

            text_width, text_height = draw.textsize(bottom_text, font)
            draw.text(((img.width - text_width) / 2, img.height - text_height - 10), bottom_text, (255, 255, 255), font=font)

            # Save the meme
            img.save("generated_meme.jpg")
            print("Meme generated successfully!")

        else:
            print("Please upload an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeGenerator(root)
    root.mainloop()
