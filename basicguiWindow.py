import tkinter as tk
from tkinter import ttk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Modern GUI Window")
window.geometry("400x300")

# Create a themed button
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))
button = ttk.Button(window, text="Click me!", command=on_button_click, style="TButton")
button.pack(pady=20)

# Create a themed label
label = ttk.Label(window, text="Welcome to a Modern GUI", font=('Helvetica', 14))
label.pack(pady=20)

# Run the main loop
window.mainloop()
