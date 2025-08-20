class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.rollnumber= roll_number
    def getName(self):
        return self.name
    def getRoll(self):
        return self.rollnumber
    
    def setName(self, name):
        self.name= name
    def setRoll(self, roll):
        self.rollnumber= roll
    
class StudentView:
    def __init__(self, Student):
        self.Student= Student
    def view(self):
        print("Name: ", self.Student.name)
        print("Roll: ", self.Student.rollnumber)
class StudentController:
    def __init__(self, name, roll):
        self.model= Student(name,roll)
        self.view= StudentView(self.model)
    def ShowStudent(self):
        self.view.view()
controller= StudentController("Omer", 20)
controller.ShowStudent()
