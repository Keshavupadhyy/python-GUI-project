import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

def display_wish():
    message = message_entry.get()
    if message:
        messagebox.showinfo("Wishing Card", f"Happy Wishes!\n\n{message}", icon='info')
    else:
        messagebox.showwarning("Warning", "Please enter a message!", icon='warning')

def choose_font():
    selected_font = font_var.get()
    font = tk.font.nametofont(selected_font)
    result_font = tk.font.askfont(font=font)
    if result_font:
        font_var.set(result_font['family'])

def choose_color():
    color = colorchooser.askcolor(title="Choose Text Color")[1]
    if color:
        text_color_var.set(color)

def choose_background():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        background_color_var.set(color)

def save_wish():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, 'w') as file:
            file.write(message_entry.get())
        messagebox.showinfo("Save Successful", "Wish saved successfully!")

# Create the main window
root = tk.Tk()
root.title("Wishing Card")

# Create a label
label = tk.Label(root, text="Enter your wish:")
label.pack(pady=10)

# Create a text entry
message_entry = tk.Entry(root, width=30)
message_entry.pack(pady=10)

# Create font and color variables
font_var = tk.StringVar()
font_var.set("TkDefaultFont")
text_color_var = tk.StringVar()
text_color_var.set("black")
background_color_var = tk.StringVar()
background_color_var.set("white")

# Create a button to display the wish
wish_button = tk.Button(root, text="Display Wish", command=display_wish)
wish_button.pack(pady=10)

# Create a button to choose font
font_button = tk.Button(root, text="Choose Font", command=choose_font)
font_button.pack(pady=5)

# Create a button to choose text color
color_button = tk.Button(root, text="Choose Text Color", command=choose_color)
color_button.pack(pady=5)

# Create a button to choose background color
background_button = tk.Button(root, text="Choose Background Color", command=choose_background)
background_button.pack(pady=5)

# Create a button to save wish
save_button = tk.Button(root, text="Save Wish", command=save_wish)
save_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
