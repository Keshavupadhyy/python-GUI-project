import tkinter as tk

def create_house():
    canvas.delete("all")  # Clear previous drawings

    # Draw the house
    canvas.create_rectangle(50, 150, 250, 350, outline="black", fill="lightblue")  # House body
    canvas.create_rectangle(120, 150, 180, 250, outline="black", fill="brown")  # Door
    canvas.create_polygon(50, 150, 150, 50, 250, 150, outline="black", fill="red")  # Roof

    # Draw windows
    canvas.create_rectangle(80, 180, 120, 220, outline="black", fill="yellow")  # Window 1
    canvas.create_rectangle(180, 180, 220, 220, outline="black", fill="yellow")  # Window 2

# Create the main window
root = tk.Tk()
root.title("Advanced House GUI")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

# Create a button to draw the house
draw_button = tk.Button(root, text="Draw Advanced House", command=create_house)
draw_button.pack()

# Run the GUI
root.mainloop()
