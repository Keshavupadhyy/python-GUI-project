import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check valid credentials (replace with a proper authentication system in a real application)
        valid_credentials = {'admin': 'password'}

        if username in valid_credentials and password == valid_credentials[username]:
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
