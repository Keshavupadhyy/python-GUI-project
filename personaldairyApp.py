import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime
from tkcalendar import DateEntry  # Install using: pip install tkcalendar


class DiaryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Diary App")

        # Create and configure the database
        self.conn = sqlite3.connect('diary.db')
        self.create_table()

        # Create UI elements
        self.label = tk.Label(master, text="Write your thoughts:")
        self.label.pack(pady=10)

        self.text_entry = tk.Text(master, height=10, width=50)
        self.text_entry.pack(pady=10)

        self.date_entry_label = tk.Label(master, text="Select Date:")
        self.date_entry_label.pack(pady=5)

        self.date_entry = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)

        self.save_button = tk.Button(master, text="Save Entry", command=self.save_entry)
        self.save_button.pack(pady=10)

        self.show_entries_button = tk.Button(master, text="Show Entries", command=self.show_entries)
        self.show_entries_button.pack(pady=10)

        self.edit_button = tk.Button(master, text="Edit Entry", command=self.edit_entry)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Entry", command=self.delete_entry)
        self.delete_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Search Entries", command=self.search_entries)
        self.search_button.pack(pady=5)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()

    def save_entry(self):
        content = self.text_entry.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Entry", "Please write something before saving.")
            return

        date = self.date_entry.get_date().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO entries (date, content) VALUES (?, ?)", (date, content))
        self.conn.commit()
        messagebox.showinfo("Entry Saved", "Your entry has been saved successfully.")

    def show_entries(self):
        entries_window = tk.Toplevel(self.master)
        entries_window.title("Diary Entries")

        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date, content FROM entries ORDER BY date DESC")
        entries = cursor.fetchall()

        if not entries:
            messagebox.showinfo("No Entries", "You haven't written any entries yet.")
            return

        for entry in entries:
            entry_text = f"{entry[1]}\n\n{entry[2]}\n{'=' * 50}\n"
            entry_label = tk.Label(entries_window, text=entry_text, justify=tk.LEFT)
            entry_label.pack(pady=10)

    def edit_entry(self):
        entry_id = simpledialog.askinteger("Edit Entry", "Enter the ID of the entry you want to edit:")
        if entry_id is not None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT content FROM entries WHERE id=?", (entry_id,))
            result = cursor.fetchone()

            if result:
                new_content = simpledialog.askstring("Edit Entry", "Edit your entry:", initialvalue=result[0])

                if new_content is not None:
                    cursor.execute("UPDATE entries SET content=? WHERE id=?", (new_content, entry_id))
                    self.conn.commit()
                    messagebox.showinfo("Entry Edited", "Your entry has been edited successfully.")
                else:
                    messagebox.showinfo("Edit Canceled", "Edit operation canceled.")
            else:
                messagebox.showwarning("Entry Not Found", f"No entry found with ID {entry_id}.")

    def delete_entry(self):
        entry_id = simpledialog.askinteger("Delete Entry", "Enter the ID of the entry you want to delete:")
        if entry_id is not None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT content FROM entries WHERE id=?", (entry_id,))
            result = cursor.fetchone()

            if result:
                confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this entry?")
                if confirmation:
                    cursor.execute("DELETE FROM entries WHERE id=?", (entry_id,))
                    self.conn.commit()
                    messagebox.showinfo("Entry Deleted", "Your entry has been deleted successfully.")
                else:
                    messagebox.showinfo("Deletion Canceled", "Deletion operation canceled.")
            else:
                messagebox.showwarning("Entry Not Found", f"No entry found with ID {entry_id}.")

    def search_entries(self):
        search_text = simpledialog.askstring("Search Entries", "Enter search text:")
        if search_text is not None:
            entries_window = tk.Toplevel(self.master)
            entries_window.title("Search Results")

            cursor = self.conn.cursor()
            cursor.execute("SELECT date, content FROM entries WHERE content LIKE ? ORDER BY date DESC",
                           ('%' + search_text + '%',))
            entries = cursor.fetchall()

            if not entries:
                messagebox.showinfo("No Results", f"No entries found containing '{search_text}'.")
                return

            for entry in entries:
                entry_text = f"{entry[0]}\n\n{entry[1]}\n{'=' * 50}\n"
                entry_label = tk.Label(entries_window, text=entry_text, justify=tk.LEFT)
                entry_label.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
