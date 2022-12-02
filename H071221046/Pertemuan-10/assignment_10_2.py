class Tontonan :
    def __init__(self, Jenis, Genre) :
        self._Jenis = Jenis
        self._Genre = Genre

    def getJenis(self) :
        return self._Jenis

    def setJenis(self, Jenis) :
        self._Jenis = Jenis
        
    def getGenre(self) :
        return self._Genre

    def setGenrel(self, Genre) :
        self._Genrel = Genre

    def membandingkan(self) :
        pass

class Film(Tontonan) :
    def __init__(self, Jenis, Genre) :
        super().__init__(Jenis, Genre)

    def membandingkan(self, target) :
        print(f"Menonton Film lebih seru dibanding menonton {target.getJenis()}!")

class Drama(Tontonan) :
    def __init__(self, Jenis, Genre) :
        super().__init__(Jenis, Genre)

    def membandingkan(self, target) :
        print(f"\nDrama lebih rumit daripada {target.getJenis()}")

a = Film("Film", 'abc')
b = Drama("Drama", 'Han')

b.membandingkan(a)
a.membandingkan(b)





#class abstrak
from abc import ABC, abstractmethod
 
class Kendaraan(ABC) :
    @abstractmethod
    def muatan(self) :
        pass
 
class Mobil(Kendaraan) :
    def muatan(self) :
        print("\nMobil dapat menampung 6 penumpang")
 
class Motor(Kendaraan) :
    def muatan(self) :
        print("Motor dapat menampung 2 penumpang\n")
r = Mobil()
r.muatan()

p = Motor()
p.muatan()
