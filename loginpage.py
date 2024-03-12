import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle  # Install ttkthemes library
from PIL import Image, ImageTk  # Install Pillow library


def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your authentication logic here
    # For simplicity, I'm using a basic check
    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Modern Login Page")

# Set a custom style using ttkthemes
style = ThemedStyle(root)
style.set_theme("equilux")  # Use a theme of your choice, make sure ttkthemes is installed

# Load and display an image (you can replace 'background_image.png' with your image)
image = Image.open("example_image_advanced.png")
photo = ImageTk.PhotoImage(image)
background_label = ttk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Create and place widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, padx=50, pady=50)

label_username = ttk.Label(frame, text="Username:")
label_password = ttk.Label(frame, text="Password:")
entry_username = ttk.Entry(frame)
entry_password = ttk.Entry(frame, show="*")
button_login = ttk.Button(frame, text="Login", command=validate_login)

label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=1, pady=10, sticky=tk.E)

# Start the main loop
root.mainloop()
