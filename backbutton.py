import tkinter as tk
from tkinter import ttk

def animate_back_button():
    for i in range(10, -1, -1):
        back_button.place(x=i*10, y=10)
        root.update_idletasks()
        root.after(30)

def on_back_button_click():
    print("Back button clicked")
    # Add your back button functionality here

root = tk.Tk()
root.title("Animated Back Button")

# Create and configure back button
back_button = ttk.Button(root, text="Back", command=on_back_button_click)
back_button.place(x=0, y=10)

# Start the animation when the window is opened
root.after(1000, animate_back_button)

root.mainloop()
