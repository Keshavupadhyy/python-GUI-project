import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct (you should replace this with your own authentication logic)
    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Colorful Login Page")

# Set window size and position
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Define colors
background_color = "#3498db"  # Blue color
label_color = "#ecf0f1"       # Light gray color
button_color = "#2ecc71"      # Green color

# Set background color
root.configure(bg=background_color)

# Create and place widgets
label_username = tk.Label(root, text="Username:", bg=background_color, fg=label_color)
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:", bg=background_color, fg=label_color)
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

login_button = tk.Button(root, text="Login", command=login, bg=button_color, fg=label_color)
login_button.pack(pady=20)

# Start the main loop
root.mainloop()
