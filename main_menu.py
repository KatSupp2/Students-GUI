from add_student import AddStudent
from print_all_student import PrintAllStudent
from search_student import SearchStudent

class MainMenu:
    def __init__(self):
        self.add_student_manager = AddStudent()
        self.current_student = None
        self.search_student = SearchStudent(self.add_student_manager, self.current_student)

    def login(self, id_no):
        for student in self.add_student_manager.allstudent:
            if student.get_id_no() == id_no:
                self.current_student = student
                self.search_student.current_student = self.current_student
                self.user_name = student.get_name()
                return True
        return False

    def register_new_student(self):
        while True:
            print("\n========== Add New Student ==========\n")
            self.add_student_manager.input_new_student()
            print("\n========== Nothing Follows ==========\n")
            another = input("Do you want to add another student? (Y/N): ").upper()
            if another != 'Y':
                break

    def print_all_students(self):
        if not self.add_student_manager.allstudent:
            print("No students have been added yet.")
        else:
            print_all_students = PrintAllStudent(self.add_student_manager.allstudent)
            print_all_students.print_all_students()

    def show_menu(self):
        self.login()
        while True:
            print("\nPlease choose from the following options:\n")
            print("1. View your information")
            print("2. View other student's information")
            print("3. Register a New Student")
            print("4. Print all students in the list")
            print("5. Exit\n")

            choice = input("Your choice: ")

            if choice == '1':
                self.search_student.view_own_info()
            elif choice == '2':
                self.search_student.view_other_student_info()
            elif choice == '3':
                self.register_new_student()
            elif choice == '4':
                self.print_all_students()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")