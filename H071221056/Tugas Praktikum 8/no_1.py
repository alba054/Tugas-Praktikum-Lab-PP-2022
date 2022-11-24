# creat class
# name = "ayu" --> Variabel biasa
# name = "nakita"  --> Variabel biasa
class person:

    def __init__(self, name, age, gender, alamat):
        self.name = name
        self.age = age
        self.gender = gender
        self.alamat = alamat
    
    def setAge(self, age) :
        self.age = age
    def getAge(self):
        return self.age
    def setName(self, name) :
        self.name = name
    def getName(self):
        return self.name
    def setGender(self, gender) :
        self.gender = gender
    def getGender(self):
        if self.gender == True :
            return "Male"
        elif self.gender == False:

            return "Female"
        else :
            return "gender harus true atau False"
    def setAlamat(self, alamat) :
        self.alamat = alamat
    def getAlamat (self) :
        return self.alamat
    def setdefaultAge(self):
        self.setAge(10)


data = person("Ayu", 18, False, "makassar")
data2 = person("nakita", 20 , True , "damai",)
print(data.getAge())
print(data.name)
print(data.getGender())
print(data.getAlamat())
print(data.name)
data.setName("lisa")
data.setAge(10)
data.setGender(3)
print(data.getGender())
data.name = "nakita"
print(data.getName())