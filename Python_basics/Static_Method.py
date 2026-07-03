class Math:
    def __init__(self, num):
        self.num = num
    
    def addtoNum(self, n):
        self.num = self.num + n
        return self.num
    
    @staticmethod
    def add(a, b):
        return a + b

a = Math(5)
print(a.num)
a.addtoNum(6)
print(a.num)
print(a.add(7,2))