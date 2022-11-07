class kubus :
    def __init__(self,panjang : float,lebar : float,tinggi : float):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def setPanjang(self,panjang : float):
        self.panjang = panjang
        
    def setLebar(self,lebar : float):
        self.lebar = lebar
        
    def setTinggi(self, tinggi: float):
        self.tinggi = tinggi
        
    def setMassa(self, massa: float):
        self.massa = massa
        
    def getMassaJenis(self):
        return self.massa / (self.panjang * self.lebar * self.tinggi) 
        
lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())
kubus = kubus(lebar, tinggi, panjang)
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())