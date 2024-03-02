import tkinter as tk
from tkinter import messagebox

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    try:
        year = int(entry.get())
        if is_leap_year(year):
            messagebox.showinfo("Result", f"{year} is a Leap Year!")
        else:
            messagebox.showinfo("Result", f"{year} is not a Leap Year.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year!")

# GUI setup
root = tk.Tk()
root.title("Leap Year Checker")

# Label
label = tk.Label(root, text="Enter a year:")
label.pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Check Leap Year", command=check_leap_year)
check_button.pack(pady=10)

# Run the main loop
root.mainloop()
