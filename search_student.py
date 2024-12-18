from tkinter import Frame, Label, Button
from student import StudentInfo

class SearchStudentUI:
    def __init__(self, parent_frame, manager, current_student=None):
        self.parent_frame = parent_frame
        self.manager = manager
        self.current_student = current_student
        self.frame = Frame(parent_frame, bg="white")

        Label(self.frame, text="Search Student Information", font=("Tahoma", 20, "bold"), bg="white").pack(pady=10)
        Button(self.frame, text="View My Information", bg="skyblue", command=self.view_my_info).pack(pady=5)
        Button(self.frame, text="View Other Students", bg="skyblue", command=self.view_other_students).pack(pady=5)

        self.info_label = Label(self.frame, text="", bg="white", justify="left")
        self.info_label.pack(pady=10)

    def view_my_info(self):
        if self.current_student:
            self.info_label.config(text=str(self.current_student))
        else:
            self.info_label.config(text="No student is currently logged in.")

    def view_other_students(self):
        students = self.manager.allstudent
        if not students:
            self.info_label.config(text="No students available.")
            return

        info_text = "\n".join(f"Name: {student.get_name()}, ID: {student.get_id_no()}" for student in students)
        self.info_label.config(text=info_text)
        self.info_label.after(1000, lambda: self.prompt_student_selection())

    def prompt_student_selection(self):
        from tkinter.simpledialog import askstring
        student_id = askstring("Search Student", "Enter Student ID to view details:")

        if student_id:
            for student in self.manager.allstudent:
                if student.get_id_no() == student_id:
                    self.info_label.config(text=f"Details:\n{student}")
                    return
            self.info_label.config(text="No student found with that ID.")

    def set_current_student(self, student):
        self.current_student = student

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()