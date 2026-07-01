class ParentClass:
    def parentmethod(self):
        print("This is the parent method")
class ChildClass(ParentClass):
    def parentmethod(self):
        print("Harry")
        super().parentmethod()
    def childmethod(self):
        print("This is the child method")
        super().parentmethod()

childObject = ChildClass()
childObject.parentmethod()
childObject.childmethod()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

harry = Programmer("Harris Ali Khan", 2501002, "Python")
print(harry.name, harry.id, harry.lang)