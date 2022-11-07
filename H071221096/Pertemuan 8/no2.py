class Kubus:
    def __init__(self, inputlebar, inputtinggi, inputpanjang, inputmassa):
        self.lebar = inputlebar
        self.tinggi = inputtinggi
        self.panjang = inputpanjang
        self.massa = inputmassa

    def setLebar(self, nilai):
        self.lebar = nilai

    def setTinggi(self, nilai):
        self.tinggi = nilai

    def setPanjang(self, nilai):
        self.panjang = nilai

    def setMassa(self, nilai):
        self.massa = nilai
    
    def getMassaJenis(self):
        volume = self.lebar*self.tinggi*self.panjang
        self.massajenis = self.massa/volume
        return self.massajenis 
        
lebar = float(input("lebar : "))
tinggi = float(input("tinggi : "))
panjang = float(input("panjang : "))
massa = float(input("massa : "))


kubus = Kubus(lebar, tinggi, panjang, massa)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa jenis", kubus.getMassaJenis())




    