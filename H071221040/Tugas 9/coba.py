class Human:
    def __init__(self, name, pos_x):
        self.nama = name
        self.__posisi = pos_x
    
    def setMovement(self, arah):
        if arah == 'L' :
            self .__posisi = self.__posisi - self._speed
        elif arah == 'R' :
            self.__posisi = self.__posisi + self._speed
    
    def getMovement(self):
        return self.__posisi
    
class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def attack(self, target):
        target._health = target._health - self._power
    
    def getPower(self):
        return self._power
    
    def getArmor(self):
        return self._armor

    def getHealth(self):
        return self._health

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health = target._health - self._power

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4

    def getSpeed(self):
        return self._speed
    
    def special(self, target):
        self.speed = 7
        self._power= 42
        target._health = target.health - self._power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.speed = 4

    def getSpeed(self):
        return self.speed

    def special(self, target):
        self.speed = 6
        target._health = target._health+150



