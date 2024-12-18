class StudentInfo:
    def __init__(self, name="", age=0, id_no="", email="", phone=""):
        self._name = name
        self._age = age
        self._id_no = id_no
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_id_no(self):
        return self._id_no

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_id_no(self, id_no):
        self._id_no = id_no

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return (f"Name: {self._name}\n"
                f"Age: {self._age}\n"
                f"ID No.: {self._id_no}\n"
                f"Email: {self._email}\n"
                f"Phone No.: {self._phone}")