class person:
    def __init__(self,name,age,Ismale):
        self.name=name
        self.age=age
        self.Ismale=Ismale

    def setAge(self,input):
        self.age=input

    def getAge(self):
        return self.age

    def setName(self,input):
        self.name=input

    def getName(self):
        return self.name

    def setGender(self,input):
        self.Ismale=input

    def getGender(self):
        return self.Ismale
while True:
    Charname=input("Input nama : ")
    Charage=int(input("Input Usia : "))
    Male=bool(input("input True/False : "))

    if Male== True or Male ==False:
        break
    else:
        print("Gender harus berupa boolean")


Charname=person(Charname,Charage,Male)
Charname.getName()
Charname.getAge()
Charname.getGender()
