import tkinter as tk
from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.now()
    birth_date = datetime(birth_year, birth_month, birth_day)

    age = current_date - birth_date
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    return years, months, days

def calculate_button_clicked():
    try:
        birth_year = int(entry_birth_year.get())
        birth_month = int(entry_birth_month.get())
        birth_day = int(entry_birth_day.get())

        years, months, days = calculate_age(birth_year, birth_month, birth_day)

        if years < 0 or months < 0 or days < 0:
            result_label.config(text="Invalid birth date. Please enter a valid date.")
        else:
            result_label.config(text=f"Your age is: {years} years, {months} months, and {days} days.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid values.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place widgets
label_birth_date = tk.Label(root, text="Enter your birth date:")
label_birth_date.pack()

label_birth_year = tk.Label(root, text="Year:")
label_birth_year.pack()
entry_birth_year = tk.Entry(root)
entry_birth_year.pack()

label_birth_month = tk.Label(root, text="Month:")
label_birth_month.pack()
entry_birth_month = tk.Entry(root)
entry_birth_month.pack()

label_birth_day = tk.Label(root, text="Day:")
label_birth_day.pack()
entry_birth_day = tk.Entry(root)
entry_birth_day.pack()

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_button_clicked)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
