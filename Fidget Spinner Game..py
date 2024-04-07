import tkinter as tk
from PIL import Image, ImageTk
import random

class FidgetSpinnerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Fidget Spinner Game")

        # Load fidget spinner image
        self.image = Image.open("spinner.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # Create canvas to display spinner
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.spinner = self.canvas.create_image(200, 200, image=self.photo)

        # Create spin button
        self.spin_button = tk.Button(root, text="SPIN", command=self.spin_spinner)
        self.spin_button.pack()

    def spin_spinner(self):
        # Rotate the spinner randomly
        angle = random.randint(0, 359)
        self.canvas.delete(self.spinner)
        rotated_image = self.image.rotate(angle)
        self.photo = ImageTk.PhotoImage(rotated_image)
        self.spinner = self.canvas.create_image(200, 200, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    game = FidgetSpinnerGame(root)
    root.mainloop()
