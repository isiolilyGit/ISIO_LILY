class Person:
    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, reg_num, student_num):
        super().__init__(name)
        self.reg_num = reg_num
        self.student_num = student_num

    def display_details(self):
        print(f"The student is: {self.name}\nReg_Number: {self.reg_num}\nStudent number: {self.student_num}")

student = Student("Ime", "23/U/0445", "2300700445")
student.display_details()
        
