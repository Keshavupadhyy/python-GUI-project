import tkinter as tk
from tkinter import ttk

def currency_converter():
    amount = float(amount_entry.get())
    from_currency = from_currency_combo.get()
    to_currency = to_currency_combo.get()

    # Exchange rates dictionary (not real-time rates)
    exchange_rates = {
        'USD': {'EUR': 0.88, 'GBP': 0.76, 'JPY': 109.98, 'INR': 74.83},
        'EUR': {'USD': 1.14, 'GBP': 0.86, 'JPY': 125.17, 'INR': 85.43},
        'GBP': {'USD': 1.32, 'EUR': 1.16, 'JPY': 144.53, 'INR': 99.53},
        'JPY': {'USD': 0.0091, 'EUR': 0.008, 'GBP': 0.0069, 'INR': 0.69},
        'INR': {'USD': 0.013, 'EUR': 0.012, 'GBP': 0.010, 'JPY': 1.45}
    }

    # Check if both currencies are in the exchange rates dictionary
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        result_label.config(text="Currency not supported")
        return

    # Perform conversion
    if from_currency == to_currency:
        converted_amount = amount
    else:
        conversion_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate

    result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create input widgets
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5)

amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=5, pady=5)

from_currency_combo = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY', 'INR'])
from_currency_combo.grid(row=1, column=1, padx=5, pady=5)
from_currency_combo.current(0)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=5, pady=5)

to_currency_combo = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY', 'INR'])
to_currency_combo.grid(row=2, column=1, padx=5, pady=5)
to_currency_combo.current(0)

convert_button = ttk.Button(root, text="Convert", command=currency_converter)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()
