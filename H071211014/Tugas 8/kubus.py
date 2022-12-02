class Kubus:
    def __init__(self,lebar,tinggi,panjang,massa):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa

    def setLebar(self,lebar):
        self.lebar = lebar
    def setTinggi(self,tingi):
        self.lebar = lebar
    def setPanjang(self,panjang):
        self.lebar = lebar
    def setMassa(self,massa):
        self.massa = massa
    def getMassaJenis(self):
        volume = self.panjang*self.lebar*self.tinggi
        p = self.massa/volume
        return p

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar,tinggi,panjang,massa)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis = ", kubus.getMassaJenis())