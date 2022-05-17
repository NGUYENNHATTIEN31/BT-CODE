from tkinter import E


class Employee:

    def __init__(self, name, id):
        self.id =id;
        self.name = name;
    def display (self):
        print("ID: %d \nName: %s" % (self.id, self.name))
emp1 =Employee("Vinh", 101)
emp1.display()
emp2 = Employee("Trung", 102)
emp2.display()   

    