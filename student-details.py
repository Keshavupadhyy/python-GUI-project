import tkinter as tk

class StudentDetailsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Details")

        self.student_name_label = tk.Label(self.master, text="Name:")
        self.student_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.student_name_entry = tk.Entry(self.master, width=20, font=('Helvetica', 14))
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.student_age_label = tk.Label(self.master, text="Age:")
        self.student_age_label.grid(row=1, column=0, padx=10, pady=10)

        self.student_age_entry = tk.Entry(self.master, width=5, font=('Helvetica', 14))
        self.student_age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.student_gender_label = tk.Label(self.master, text="Gender:")
        self.student_gender_label.grid(row=2, column=0, padx=10, pady=10)

        self.student_gender_var = tk.StringVar()
        self.student_gender_var.set("Male")
        self.student_gender_dropdown = tk.OptionMenu(self.master, self.student_gender_var, "Male", "Female", "Other")
        self.student_gender_dropdown.grid(row=2, column=1, padx=10, pady=10)

        self.student_department_label = tk.Label(self.master, text="Department:")
        self.student_department_label.grid(row=3, column=0, padx=10, pady=10)

        self.student_department_var = tk.StringVar()
        self.student_department_var.set("Computer Science")
        self.student_department_dropdown = tk.OptionMenu(self.master, self.student_department_var, "Computer Science", "Electrical Engineering", "Mechanical Engineering")
        self.student_department_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.button_submit = tk.Button(self.master, text="Submit", font=('Helvetica', 14), command=self.submit_data)
        self.button_submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def submit_data(self):
        name = self.student_name_entry.get()
        age = self.student_age_entry.get()
        gender = self.student_gender_var.get()
        department = self.student_department_var.get()

        print(f"Name: {name}, Age: {age}, Gender: {gender}, Department: {department}")

root = tk.Tk()
student_details_app = StudentDetailsApp(root)
root.mainloop()