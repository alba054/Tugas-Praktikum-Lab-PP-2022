class Person :
    def __init__(self, nama, umur, gender) :
        self.name = nama
        self.age = umur
        self.isMale = gender


    def setName(self, nama) :
        self.name = nama 
    def getName(self) :
        print(f"Nama : {self.name}")

    def setAge(self, umur) :
        self.age = umur
    def getAge(self) :
        print(f"Umur : {self.age}")

    def setGender(self, gender) :
        self.isMale = gender
    def getGender(self) :
        if self.isMale == True :
            print('Laki-laki')
        else :
            self.isMale == False
            print('Perempuan')
    
nakita = Person ('Nakita', 18, False)
nakita.getName ()
nakita.getAge ()
nakita.getGender ()
