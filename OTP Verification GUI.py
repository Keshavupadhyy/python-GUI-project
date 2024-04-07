import tkinter as tk
from tkinter import messagebox
import random

class OTPVerificationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification")

        # Generate OTP
        self.otp = self.generate_otp()

        # OTP Label and Entry
        self.otp_label = tk.Label(root, text="Enter OTP:")
        self.otp_label.pack()
        self.otp_entry = tk.Entry(root)
        self.otp_entry.pack()

        # Verify Button
        self.verify_button = tk.Button(root, text="Verify", command=self.verify_otp)
        self.verify_button.pack()

    def generate_otp(self):
        # Generate a 6-digit OTP
        return str(random.randint(100000, 999999))

    def verify_otp(self):
        # Get the entered OTP
        entered_otp = self.otp_entry.get()

        # Compare entered OTP with generated OTP
        if entered_otp == self.otp:
            messagebox.showinfo("Success", "OTP verification successful!")
        else:
            messagebox.showerror("Error", "Invalid OTP. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    otp_verification_gui = OTPVerificationGUI(root)
    root.mainloop()
