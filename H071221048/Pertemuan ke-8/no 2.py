class kubus:
    massajenis=0
    def __init__(self,lebar,tinggi,panjang,massa):
        self.lebar=lebar
        self.tinggi=tinggi
        self.panjang=panjang
        self.massa=massa
        # self.volume=self.lebar*self.panjang*self.tinggi
    
    def get_volume(self):
        volume=self.lebar*self.panjang*self.tinggi

        return volume
    
    def get_massajenis(self):
        massajenis=self.get_volume()*self.massa
        return massajenis
        
box=kubus(1,1,1,0)
print(box.get_volume())
box.tinggi=2
print(box.get_volume())
box.get_volume()

