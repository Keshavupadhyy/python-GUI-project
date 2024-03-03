import random
import string
from tkinter import Tk, Label, Entry, Button

class OTPVerification:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification")

        self.otp = ''.join(random.choices(string.digits, k=6))
        self.entry_otp = Entry(self.master, width=10, font=('Helvetica', 24), borderwidth=2)
        self.entry_otp.grid(row=0, column=0, padx=10, pady=10)

        self.label_otp = Label(self.master, text="Enter OTP:", font=('Helvetica', 18), borderwidth=2)
        self.label_otp.grid(row=0, column=1, padx=10, pady=10)

        self.button_verify = Button(self.master, text="Verify", font=('Helvetica', 18), command=self.verify_otp)
        self.button_verify.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.label_result = Label(self.master, text="", font=('Helvetica', 18), borderwidth=2)
        self.label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def verify_otp(self):
        if self.entry_otp.get() == self.otp:
            self.label_result.config(text="OTP verified!")
        else:
            self.label_result.config(text="Invalid OTP")

root = Tk()
otp_verification = OTPVerification(root)
root.mainloop()