import tkinter as tk
from tkinter import messagebox
from plyer import notification


def show_notification():
    title = entry_title.get()
    message = entry_message.get()

    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )


def show_gui():
    root = tk.Tk()
    root.title("Desktop Notifications")

    label_title = tk.Label(root, text="Title:")
    label_title.pack()

    entry_title = tk.Entry(root)
    entry_title.pack()

    label_message = tk.Label(root, text="Message:")
    label_message.pack()

    entry_message = tk.Entry(root)
    entry_message.pack()

    notify_button = tk.Button(root, text="Show Notification", command=show_notification)
    notify_button.pack()

    root.mainloop()


if __name__ == "__main__":
    show_gui()
