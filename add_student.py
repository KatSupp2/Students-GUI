from tkinter import Frame, Label, Entry, Button, StringVar
from student import StudentInfo

class AddStudent:
    def __init__(self):
        self.allstudent = []
        self.load_students()

    def add_student(self, student):
        self.allstudent.append(student)
        print(f"Added student {student.get_name()} to the list.")
        self.save_students()

    def save_students(self):
        with open('student_list.txt', 'w') as file:
            for student in self.allstudent:
                file.write(f"{student.get_name()},{student.get_age()},{student.get_id_no()},{student.get_email()},{student.get_phone()}\n")

    def load_students(self):
        try:
            with open('student_list.txt', 'r') as file:
                for line in file:
                    name, age, id_no, email, phone = line.strip().split(',')
                    student = StudentInfo(name, age, id_no, email, phone)
                    self.allstudent.append(student)
        except FileNotFoundError:
            print("No student data file found.")

class AddStudentUI:
    def __init__(self, parent_frame, manager):
        self.parent_frame = parent_frame
        self.manager = manager
        self.frame = Frame(parent_frame, bg="white")

        self.name_var = StringVar()
        self.age_var = StringVar()
        self.id_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()

        Label(self.frame, text="Add New Student", font=("Tahoma", 20, "bold"), bg="white").pack(pady=10)
        
        Label(self.frame, text="Name:", bg="white").pack()
        Entry(self.frame, textvariable=self.name_var).pack()

        Label(self.frame, text="Age:", bg="white").pack()
        Entry(self.frame, textvariable=self.age_var).pack()

        Label(self.frame, text="ID:", bg="white").pack()
        Entry(self.frame, textvariable=self.id_var).pack()

        Label(self.frame, text="Email:", bg="white").pack()
        Entry(self.frame, textvariable=self.email_var).pack()

        Label(self.frame, text="Phone:", bg="white").pack()
        Entry(self.frame, textvariable=self.phone_var).pack()

        Button(self.frame, text="Register", bg="skyblue", command=self.add_student).pack(pady=10)

        self.status_label = Label(self.frame, text="", bg="white", fg="green")
        self.status_label.pack()

    def add_student(self):
        student_data = [
            self.name_var.get(),
            self.age_var.get(),
            self.id_var.get(),
            self.email_var.get(),
            self.phone_var.get()
        ]

        if all(student_data):
            student = StudentInfo(*student_data)
            self.manager.add_student(student)
            self.clear_entries()
            self.status_label.config(text="Student Added Successfully!", fg="green")
        else:
            self.status_label.config(text="All fields are required!", fg="red")

    def clear_entries(self):
        self.name_var.set("")
        self.age_var.set("")
        self.id_var.set("")
        self.email_var.set("")
        self.phone_var.set("")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()