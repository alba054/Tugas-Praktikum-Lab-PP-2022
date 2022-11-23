class Human:
    def __init__(self,nama,postX):
        self.name = nama
        self.__postX = postX
        # self._armor = 0
        # self._power = 0
        # self._health = 0
        # self._speed = 0
    
    def move(self,newPosition):
        if newPosition == "L" or newPosition == "l":
            self.__postX -= 1
        elif newPosition == "R" or newPosition == "r":
            self.__postX += 1
        else :
            print("hanya menerima R dan L")
            
    def setName(self,name):
        self.name = name 
        
    def getName(self):
        return self.name
    
class Hero(Human):
    def __init__(self,name,postX):
        super().__init__(name,postX)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
        
    def attack(self,target):
        target._health -= self._power
        
    def setPower(self,newPower):
        self._power = newPower
        
    def setArmor(self,newArmor):
        self._armor = newArmor
        
    def setHealth(self,newHealth):
        self._health = newHealth
        
    def setSpeed(self,newSpeed):
        self._speed = newSpeed
        
    def getPower(self):
        return self._power
        
    def getArmor(self):
        return self._armor
        
    def getHealth(self):
        return self._health
        
    def getSpeed(self):
        return self._speed
        
class Warrior(Hero):
    def __init__(self,name,postX):
        super().__init__(name,postX)
        self._power = 26
        self._armor = 30
        
    def special(self,target):
        self._power = 32
        self._armor = 45
        target._health -= self._power
        
class Assassin(Hero):
    def __init__(self,name,postX):
        super().__init__(name,postX)
        self._power = 35
        self.speed = 4
        
    def special(self,target):
        self._power = 42
        self.speed = 7
        target._health -= self._power
        
class Support(Hero):
    def __init__(self,name,postX):
        super().__init__(name,postX)
        self._health = 500
        self._armor = 8
        self.speed = 4
            
    def special(self,target):
        target._health += 150
        self.speed = 8
        
warrior = Warrior("bambang", postX=10)
assassin = Assassin("joko", postX=25)
support = Support("udin",postX=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())