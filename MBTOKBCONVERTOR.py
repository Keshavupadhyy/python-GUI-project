import tkinter as tk

def convert_mb_to_kb():
    try:
        mb_value = float(entry_mb.get())
        kb_value = mb_value * 1024
        label_result.config(text=f"{mb_value} MB is {kb_value} KB")
    except ValueError:
        label_result.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("MB to KB Converter")

# Create widgets
label_instruction = tk.Label(root, text="Enter MB:")
entry_mb = tk.Entry(root)
button_convert = tk.Button(root, text="Convert", command=convert_mb_to_kb)
label_result = tk.Label(root, text="Result will be displayed here")

# Place widgets in the window
label_instruction.grid(row=0, column=0, padx=10, pady=10)
entry_mb.grid(row=0, column=1, padx=10, pady=10)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
