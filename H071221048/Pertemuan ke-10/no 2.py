class Animal:
    def __init__(self,name):
        self._name=name
    
    def move(self):
        print(f"{self.name} bergerak")

    def turu(self):
        print(f"{self.name} Tidur")
    
class Pisces(Animal):
    def __init__(self, name,deepness):
        super().__init__(name)
        self.__deepness=deepness

    def move(self):
        print(f"{self.name} Berenang")

    def kedalaman(self):
        print(f"{self.name} Berada pada kedalaman {self.__deepness} meter ")

    def Migrate(self,input):
        print(f"{self.name} bermigrasi ke {input}")
    
class Aves(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f"{self.name} Terbang ")

    def fly(self):
        print(f"{self.name} Terbang")




