class Animal:
    def __init__(self,nama,jenis):
        pass
    
    def bergerak(self):
        pass
    
class Mamalia:
    def __init__(self,nama,jenis):
        self._nama = nama
        self.jenis = jenis
    
    def bergerak(self):
        print(f"{self.nama} bergerak menggunakan kaki")