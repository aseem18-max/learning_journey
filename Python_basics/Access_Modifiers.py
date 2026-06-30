'''
#public access modifiers
class Employee:
    def __init__(self):
        self.name = "Harry"
a = Employee()
print(a.name)
'''
'''
#private access modifiers
class Employee:
    def __init__(self):
        self.__name = "Harry"
b = Employee()
print(b._Employee__name)
print(dir(b))
'''
class Student:
    def __init__(self):
        self._name = "Harry"
    def _funname(self):
        return "CodeWithHarry"
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
print(obj._name)
print(obj._funname())
print(obj1._name)
print(obj1._funname())
print(dir(obj))