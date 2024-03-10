import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}")
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Colorful Form")

# Create and configure the form elements
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)

entry_age = tk.Entry(root, width=30)
entry_age.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white")
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
