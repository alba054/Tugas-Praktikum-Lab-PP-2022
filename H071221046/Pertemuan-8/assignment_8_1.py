class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age

    def setisMale(self, isMale):
        self.isMale = isMale

    def getisMale(self):
        return self.isMale
    
# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age  : "))
# ismale = eval(input("Are You Male?   : "))

name = "Najwa Hanana"
age = 19
ismale = False

najwa = Person(name, age, ismale)

print(najwa.getName())
print(najwa.getAge())
print(najwa.getisMale())