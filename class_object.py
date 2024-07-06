class Student:
    def __init__(self):
        self.Student_name = ""
        self.Registration_no = ""
    def display (self):
        print("Student Name : " ,  self.Student_name)
        print("Registration No : " ,  self.Registration_no)

STDdetails = Student()

STDdetails.Student_name = "Sree Chandana"
STDdetails.Registration_no = "15UCS1522"

STDdetails.display()
