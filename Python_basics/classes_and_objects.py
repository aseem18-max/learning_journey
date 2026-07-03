class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Aseem"
a.occupation = "Backend Developer"
a.networth = 20
a.info()
b=Person()
b.info()

