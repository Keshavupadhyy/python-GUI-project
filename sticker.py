import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class StickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticker App")

        # Initialize variables
        self.image_path = ""
        self.sticker_path = ""

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Image display
        self.image_label = tk.Label(self.root, text="Image:")
        self.image_label.pack()

        self.image_canvas = tk.Canvas(self.root, width=400, height=400)
        self.image_canvas.pack()

        # Button to load image
        self.load_image_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_image_button.pack()

        # Sticker display
        self.sticker_label = tk.Label(self.root, text="Sticker:")
        self.sticker_label.pack()

        self.sticker_canvas = tk.Canvas(self.root, width=100, height=100)
        self.sticker_canvas.pack()

        # Button to load sticker
        self.load_sticker_button = tk.Button(self.root, text="Load Sticker", command=self.load_sticker)
        self.load_sticker_button.pack()

        # Button to apply sticker
        self.apply_sticker_button = tk.Button(self.root, text="Apply Sticker", command=self.apply_sticker)
        self.apply_sticker_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            image = Image.open(self.image_path)
            image.thumbnail((400, 400))
            self.tk_image = ImageTk.PhotoImage(image)
            self.image_canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.image_canvas.config(width=self.tk_image.width(), height=self.tk_image.height())

    def load_sticker(self):
        file_path = filedialog.askopenfilename(title="Select Sticker", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.sticker_path = file_path
            sticker = Image.open(self.sticker_path)
            sticker.thumbnail((100, 100))
            self.tk_sticker = ImageTk.PhotoImage(sticker)
            self.sticker_canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_sticker)
            self.sticker_canvas.config(width=self.tk_sticker.width(), height=self.tk_sticker.height())

    def apply_sticker(self):
        if self.image_path and self.sticker_path:
            image = Image.open(self.image_path)
            sticker = Image.open(self.sticker_path)

            # You can implement the logic to apply the sticker to the image here
            # For example, using the paste() method from the PIL library.

            # Updated image with sticker applied
            updated_image = image.paste(sticker, (50, 50), sticker)

            # Display the updated image (this is just a simple example, you may need to update this part)
            self.tk_updated_image = ImageTk.PhotoImage(updated_image)
            self.image_canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_updated_image)
            self.image_canvas.config(width=self.tk_updated_image.width(), height=self.tk_updated_image.height())

if __name__ == "__main__":
    root = tk.Tk()
    app = StickerApp(root)
    root.mainloop()
