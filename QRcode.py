import tkinter as tk
from tkinter import ttk
import qrcode


def generate_qr_code():
    data = entry.get()
    if not data:
        status_label.config(text="Please enter data.")
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode.png')

        status_label.config(text="QR Code generated successfully!")


# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
label = ttk.Label(root, text="Enter data:")
label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry = ttk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

status_label = ttk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
