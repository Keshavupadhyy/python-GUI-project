import tkinter as tk
from tkinter import colorchooser


def round_color(rgb):
    rounded_rgb = tuple(round(val / 255) * 255 for val in rgb)
    return rounded_rgb


def choose_color():
    color = colorchooser.askcolor()[0]
    if color:
        rounded_color = round_color(color)
        result_label.config(text=f'Rounded Color: {rounded_color}',
                            bg=f'#{rounded_color[0]:02X}{rounded_color[1]:02X}{rounded_color[2]:02X}')


# Create the main window
root = tk.Tk()
root.title("Color Rounding Tool")

# Create and configure widgets
choose_color_button = tk.Button(root, text="Choose Color", command=choose_color)
choose_color_button.pack(pady=10)

result_label = tk.Label(root, text="Rounded Color: ", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
