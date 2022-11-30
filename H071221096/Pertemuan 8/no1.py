class Person:
    def __init__(self, nama, umur, gender, berat, tinggi):
        self.name = nama
        self.age = umur
        self.isMale = gender
        self.weight = berat
        self.height = tinggi

    def getName(self):
        return self.name
    def setName(self, nilai):
        self.name = nilai

    def getAge(self):
        return self.age
    def setAge(self, nilai):
        self.age = nilai

    def getisMale(self):
        return self.isMale
    def setisMale(self, nilai):
        self.isMale = nilai

    def getWeight(self):
        return self.weight
    def setWeight(self, nilai):
        self.weight = nilai

    def getHeight(self):
        return self.height
    def setHeight(self, nilai):
        self.height = nilai
    
    def HitungBMI(self):
        konversi = self.height / 100
        self.hitungBMI = self.weight/ (konversi**2)
        if self.hitungBMI < 18.5:
            print("Kurang berat badan")
        elif self.hitungBMI >= 18.5 and self.hitungBMI <= 22.9:
            print("Normal")
        elif self.hitungBMI >= 23 and self.hitungBMI <= 24.9:
            print("Kelebihan berat badan")
        elif self.hitungBMI >= 25 and self.hitungBMI <=  29.9:
            print("Obesitas tingkat 1")
        elif self.hitungBMI > 30:
            print("Obesitas tingkat 2")
        return self.hitungBMI

inputNama = str(input("nama : "))
inputUmur = int(input("umur : "))
inputGender = str(input("gender : "))
inputberatbadan = int(input("berat badan : "))
inputtinggibadan = int(input("tinggi badan : "))

orang = Person(inputNama, inputUmur, inputGender, inputberatbadan, inputtinggibadan)

print(orang.getName())
print(orang.getAge())
print(orang.getisMale())
print(orang.HitungBMI())


