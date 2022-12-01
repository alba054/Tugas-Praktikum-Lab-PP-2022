print("""
Pada program ini,terdapat 4 hero,yakni:
1.Natalia(Assasin)
2.Zilong(Warrior)
3.Estes(Support)
4.Angela(Support)""")
print("Setiap Hero akan menyerang secara bergantian satu sama lain")
class Human:
    def __init__(self,name,position):
        self.name=name
        self.__pos=position
    def get_pos (self):
        return self.__pos
    def movement (self,input):
        if input =="R":
            self.__pos+=self._speed
        if input =="L":
            self.__pos-=self._speed
    

class Hero(Human):
    def __init__ (self,name,position):
        super().__init__(name,position)
        self._power=15
        health=400
        self._health=health
        self._armor=15
        self._speed=3
    


    def attack(self,target):
        target._health-=self._power
    
        
    def GetInfo(self):
        print(f"Hero {self.name} Power {self._power} HP {self._health}",self.get_pos())
        

class Warrior(Hero):
    def __init__ (self,name,position):
        super().__init__(name,position)
        self._power=26
        self._armor=30
    def ShowInfo (self):
        print(f"Hero {self.name} Power {self._power} HP {self._health} speed {self._speed} ")

    def Special(self,target):
        self._armor=45
        self._power=32
        target._health-=self._power
        self._power=15
        self._armor=15
class Assasin(Hero):
    def __init__ (self,name,position):
        super().__init__(name,position)
        self._power=35
        self._speed=4
    def ShowInfo (self):
        print(f"Hero {self.name} Power {self._power} HP {self._health} speed {self._speed} ")
    def Special(self,target):
        self._speed=7
        self._power=42
        target._health-=self._power
        self._power=15
        self._speed=3

class Support(Hero):
    def __init__ (self,name,position):
        super().__init__(name,position)
        self._power=500
        self._armor=8
        self._speed=4
    def Special(self,target):
        self._speed=6
        target._health+=150
        self._speed=3
    def ShowInfo (self):
        print(f"Hero {self.name} Power {self._power} HP {self._health} speed {self._speed} ")

Natalia=Assasin("Natalia",10)
Zilong=Warrior("Zilong",-10)
Estes=Support("Estes",-2)
Angela=Support("Angela",2)
print("Command : ")
print("""
1=Bergerak
2=Attack
3=Special
4=Perlihatkan Status Hero""")
n=0
while True:
    print("Giliran Natalia !\n")
    c=input("Command : ")
    if c=="1":
        d=input("L/R ")
        if d=="L":
            Natalia.movement("L")
        elif d=="R":
            Natalia.movement("R")
        else:
            print("Gerakan tidak valid")
    elif c=="2":
        t=int(input("Target : "))

        if t==2:
            Natalia.attack(Zilong)
            print("Natalia menyerang Zilong")
            
        elif t==3:
            Natalia.attack(Estes)
            print("Natalia menyerang Estes")
            
        elif t==4:
            Natalia.attack(Angela)
            print("Natalia menyerang Angela")
            
        else:
            print("Input sesuai nomor hero")
            
    elif c=="3":
        t=int(input("Target : "))
        while True:
            try:
                if t==2:
                    Natalia.Special(Zilong)
                    print("Natalia menggunakan skill kepada Zilong")
                    break
                elif t==3:
                    Natalia.Special(Estes)
                    print("Natalia menggunakan skill kepada Estes")
                    break
                elif t==4:
                    Natalia.Special(Angela)
                    print("Natalia menggunakan skill kepada Angela")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="4":
        Natalia.ShowInfo()
    print("Giliran Zilong !\n")
    c=input("Command : ")
    if c=="1":
        d=input("L/R ")
        if d=="L":
            Zilong.movement("L")
        elif d=="R":
            Zilong.movement("R")
        else:
            print("Gerakan tidak valid")
    elif c=="2":
        t=int(input("Target : "))
        while True:
            try:
                if t==1:
                    Zilong.attack(Natalia)
                    print("Zilong menyerang Natalia")
                    break
                elif t==3:
                    Zilong.attack(Estes)
                    print("Zilong menyerang Estes")
                    break
                elif t==4:
                    Zilong.attack(Angela)
                    print("Zilong menyerang Angela")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="3":
        t=int(input("Target : "))
        while True:
            try:
                if t==1:
                    Zilong.Special(Natalia)
                    print("Zilong menggunakan skill kepada Natalia")
                    break
                elif t==3:
                    Zilong.Special(Estes)
                    print("Zilong menggunakan skill kepada Estes")
                    break
                elif t==4:
                    Zilong.Special(Angela)
                    print("Zilong menggunakan skill kepada Angela")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="4":
        Zilong.ShowInfo()
    
    print("Giliran Estes !\n")
    c=input("Command : ")
    if c=="1":
        d=input("L/R ")
        if d=="L":
            Estes.movement("L")
        elif d=="R":
            Estes.movement("R")
        else:
            print("Gerakan tidak valid")
    elif c=="2":
        t=int(input("Target : "))
        while True:
            
            if t==1:
                Estes.attack(Natalia)
                print("Estes menyerang Natalia")
                break
            elif t==2:
                Estes.attack(Zilong)
                print("Estes menyerang Zilong")
                break
            elif t==4:
                Estes.attack(Angela)
                print("Estes menyerang Angela")
                break
            else:
                print("Input sesuai nomor hero")
    elif c=="3":
        t=int(input("Target : "))
        while True:
            try:
                if t==1:
                    Estes.Special(Natalia)
                    print("Estes menggunakan skill kepada Natalia")
                    break
                elif t==2:
                    Estes.Special(Zilong)
                    print("Estes menggunakan skill kepada Zilong")
                    break
                elif t==4:
                    Estes.Special(Angela)
                    print("Estes menggunakan skill kepada Angela")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="4":
        Estes.ShowInfo()
    print("Giliran Angela !\n")
    c=input("Command : ")
    if c=="1":
        d=input("L/R ")
        if d=="L":
            Angela.movement("L")
        elif d=="R":
            Angela.movement("R")
        else:
            print("Gerakan tidak valid")
    elif c=="2":
        t=int(input("Target : "))
        while True:
            try:
                if t==1:
                    Angela.attack(Natalia)
                    print("Angela menyerang Natalia")
                    break
                elif t==2:
                    Angela.attack(Zilong)
                    print("Angela menyerang Zilong")
                    break
                elif t==3:
                    Angela.attack(Estes)
                    print("Angela menyerang Estes")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="3":
        t=int(input("Target : "))
        while True:
            try:
                if t==1:
                    Angela.Special(Natalia)
                    print("Angela menggunakan skill kepada Natalia")
                    break
                elif t==2:
                    Angela.Special(Zilong)
                    print("Angela menggunakan skill kepada Zilong")
                    break
                elif t==3:
                    Angela.Special(Estes)
                    print("Angela menggunakan skill kepada Estes")
                    break
            except:
                print("Input sesuai nomor hero")
    elif c=="4":
        Angela.ShowInfo()

    else:
        print("Giliran di skip")
    n+=1
    inp=int(input("""Apakah anda masih ingin bermain? :
    1 : Ya
    2 : Tidak """))
    if inp==1:
        pass

    elif inp== 2:
        break 


    


                

    
    