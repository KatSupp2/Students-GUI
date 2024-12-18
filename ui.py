from tkinter import Tk, Frame, Button, Label, Entry, messagebox

from add_student import AddStudent, AddStudentUI
from search_student import SearchStudentUI
from print_all_student import PrintAllStudentsUI

class MainUI:
    def __init__(self):
        self.win = Tk()
        self.win.title("Student Management System")
        self.win.geometry("840x480")
        self.center_window()

        self.main_frame = Frame(self.win, bg="#D2B48C")
        self.main_frame.pack(fill="both", expand=True)

        self.main_menu = AddStudent()
        self.current_student = None

        self.show_login()

    def center_window(self):
        width = 840
        height = 480
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.win.geometry(f'{width}x{height}+{x}+{y}')

    def show_login(self):
        self.clear_frames()
        Label(self.main_frame, text="Login", font=("Tahoma", 30, "bold"), bg="#D2B48C", fg="#4B3D3D").pack(pady=20)

        Label(self.main_frame, text="Student ID:", bg="#D2B48C", fg="#4B3D3D").pack(pady=10)
        self.id_entry = Entry(self.main_frame, font=("Tahoma", 14))
        self.id_entry.pack(pady=10)

        Button(self.main_frame, text="Login", command=self.login, bg="#8B4513", fg="white", font=("Tahoma", 14)).pack(pady=20)

    def login(self):
        student_id = self.id_entry.get().strip()
        for student in self.main_menu.allstudent:
            if student.get_id_no() == student_id:
                self.current_student = student
                messagebox.showinfo("Success", f"Welcome {student.get_name()}!")
                self.show_main_menu()
                return
        messagebox.showerror("Error", "Student ID not found.")

    def show_main_menu(self):
        self.clear_frames()
        Label(self.main_frame, text="Main Menu", font=("Tahoma", 30, "bold"), bg="#D2B48C", fg="#4B3D3D").pack(pady=20)

        button_frame = Frame(self.main_frame, bg="#D2B48C")
        button_frame.pack(pady=10)

        Button(button_frame, text="Add Student", command=self.show_add_student, bg="#8B4513", fg="white", font=("Tahoma", 14)).grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Search Student", command=self.show_search_student, bg="#8B4513", fg="white", font=("Tahoma", 14)).grid(row=0, column=1, padx=10, pady=10)
        Button(button_frame, text="View All Students", command=self.show_print_all_students, bg="#8B4513", fg="white", font=("Tahoma", 14)).grid(row=1, column=0, padx=10, pady=10)
        Button(button_frame, text="Logout", command=self.show_login, bg="#8B4513", fg="white", font=("Tahoma", 14)).grid(row=1, column=1, padx=10, pady=10)
        Button(button_frame, text="Exit", command=self.win.quit, bg="#8B4513", fg="white", font=("Tahoma", 14)).grid(row=2, columnspan=2, pady=20)

    def show_add_student(self):
        self.clear_frames()
        self.add_student_ui = AddStudentUI(self.main_frame, self.main_menu)
        self.add_student_ui.show()
        Button(self.main_frame, text="Back", command=self.show_main_menu, bg="#8B4513", fg="white", font=("Tahoma", 14)).pack(pady=20)

    def show_search_student(self):
        self.clear_frames()
        self.search_student_ui = SearchStudentUI(self.main_frame, self.main_menu)
        self.search_student_ui.set_current_student(self.current_student)
        self.search_student_ui.show()
        Button(self.main_frame, text="Back", command=self.show_main_menu, bg="#8B4513", fg="white", font=("Tahoma", 14)).pack(pady=20)

    def show_print_all_students(self):
        self.clear_frames()
        self.print_all_students_ui = PrintAllStudentsUI(self.main_frame, self.main_menu.allstudent)
        self.print_all_students_ui.show()
        Button(self.main_frame, text="Back", command=self.show_main_menu, bg="#8B4513", fg="white", font=("Tahoma", 14)).pack(pady=20)

    def clear_frames(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

main = MainUI()
main.win.mainloop()