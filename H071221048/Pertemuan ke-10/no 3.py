class Player:
    def __init__(self,name,role):
        self.name =name
        self.role=role
        self.level=1
        self.damage=100
        self.hp=1000
        self.energy=100
        self.money=3000
        self.items=[]

    def ShowStatus (self):
        return self.name,self.role,self.level,self.damage,self.hp,self.energy,self.money
    
    def ShowItems(self):
        return self.items

    def getDamage(self,rcvd):
        print(f"{self} menerima damage sebesar {rcvd} ")
        self.hp-=rcvd
    
    def attack(self,target):
        target.getDamage(target,self.damage)
        print(f"{self.name} menyerang {target} ")

    
    def healing(self):
        self.hp+=self.damage/2
        print(f"{self.name} melakukan healing sebesar {self.damage/2}")
    

    def use(self,items):
        if items.name in self.items:
            self.items.remove(items.name)
            self.damage+=items.atk
            self.hp+=items.hp
            print(f"{self.name} menggunakan {items.name}")
        
        else:
            print("Anda tidak memiliki item ini")
    
    def buy(self,items):
        self.money-=items.price
        print(f"{self.name} membeli {items.name} dengan harga {items.price}")
        self.items.append(items.name)

    def sell(self,items):
        if items.name in self.items:
            self.money+=items.prince*3/4
            self.items.remove(items.name)
            print (f"{self.name} dijual dengan {items.prince*3/4}")
        
    

    def destroy (self,items):
        if items.name in self.items:
            self.items.remove(items.name)
            print(f"{items.name} dihancurkan ")
        else:
            print("Anda Tidak memiliki item ini")

class items:
    def __init__(self,name,price,atk,hp):
        self.name=name
        self.price=price
        self.atk=atk
        self.hp=hp

Sword=items("Sword",1200,200,10)
Spear=items("Spear",1000,140,10)
Bow=items("Bow",1500,250,5)
Shield=items("Shield",800,40,300)



print("""
Selamat datang di program 
pada program ini,anda akan bermain sebagai player
anda diharuskan untuk mengeliminasi player lain untuk menang.
Pada program telah disediakan atribut default dan items yang dapat mengubah atribut default
items tersebut adalah:
Sword,Spear,Bow dan Shield""")

Naruto=Player("Naruto","Ninja")

print(Naruto.ShowItems())
print(Naruto.ShowStatus())
print(Naruto.use(Sword))
print(Naruto.ShowItems())
print(Naruto.ShowStatus())