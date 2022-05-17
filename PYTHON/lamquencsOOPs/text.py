#Tạo đối tượng trong py
class Employee:
    id = 10
    name = "The Mac"
    def display(self):
           print("ID: %d \nName: %s" % (self.id, self.name))
emp = Employee()
emp.display


