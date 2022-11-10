lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

class BALOK :
    def __init__(self, lebar, tinggi, panjang) :
        self.wide = lebar
        self.height = tinggi
        self.long = panjang
    
    def setMassa(self, massa) :
        self.weith = massa
    def getMassaJenis(self) :
        return self.weith/(self.long*self.height*self.wide)

balok = BALOK (lebar, tinggi, panjang)
balok.setMassa(massa)
print("Massa Jenis =", balok.getMassaJenis())
balok.setMassa(massa*2)
print("Massa Jenis =", balok.getMassaJenis())
    