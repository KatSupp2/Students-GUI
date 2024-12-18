from tkinter import Tk, Frame, Button, Text, Scrollbar, END, Label

class PrintAllStudent:
    def __init__(self, students):
        self.students = students

    def print_all_students(self):
        if not self.students:
            print("No students to display.")
        else:
            print("\n========== List of All Students ==========")
            for student in self.students:
                print(student)
                print()
            print("========== Nothing Follows ==========\n")
            
class PrintAllStudentsUI:
    def __init__(self, parent_frame, students):
        self.frame = Frame(parent_frame)
        self.students = students

        Label(self.frame, text="List of All Students", font=("Tahoma", 20, "bold")).pack(pady=10)

        self.text_area = Text(self.frame, wrap='word', height=15, width=50)
        self.text_area.pack(pady=10)

        scrollbar = Scrollbar(self.frame, command=self.text_area.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_area['yscrollcommand'] = scrollbar.set

        Button(self.frame, text="Show All Students", command=self.print_all_students).pack(pady=5)

    def print_all_students(self):
        self.text_area.delete(1.0, END)
        if not self.students:
            self.text_area.insert(END, "No students to display.")
        else:
            self.text_area.insert(END, "========== List of All Students ==========\n")
            for student in self.students:
                self.text_area.insert(END, f"{student}\n")
            self.text_area.insert(END, "========== Nothing Follows ==========\n")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()