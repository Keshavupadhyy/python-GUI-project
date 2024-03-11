import tkinter as tk

def on_button_click():
    print("Button clicked!")

def animate_button():
    current_color = button.cget("background")
    new_color = "red" if current_color == "green" else "green"
    button.configure(background=new_color)
    root.after(500, animate_button)

# Create the main window
root = tk.Tk()
root.title("Animated Button")

# Create the button
button = tk.Button(root, text="Click me", command=on_button_click, width=20, height=2, background="green")
button.pack(pady=20)

# Start the button animation
animate_button()

# Start the Tkinter event loop
root.mainloop()
