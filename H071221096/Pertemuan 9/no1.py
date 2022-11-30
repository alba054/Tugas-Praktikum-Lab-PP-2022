class Human:
    def __init__(self, nama, posisi):
        self.nama = nama
        self._posisi = posisi
        self.speed = 1

    def movement(self, arah):
        if arah == "L":
            self._posisi -= self.speed
        elif arah == "R":
            self._posisi += self.speed

    def setPosisi(self, newPosisi):
        self._posisi = newPosisi

    def getPosisi(self):
        return self._posisi

class Hero(Human):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._health = 400
        self._power = 15
        self._armor = 15
        self._speed = 3

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, newSpeed):
        self._speed = newSpeed

    def setHealth(self, newHealth):
        self._health = newHealth

    def getHealth(self):
        return self._health
    
    def setPower(self, newPower):
        self._power = newPower

    def getPower(self):
        return self._power
    
    def setArmor(self, newArmor):
        self._armor = newArmor

    def getArmor(self):
        return self._armor
    
    def setSpeed(self, newSpeed):
        self._speed = newSpeed

    def getSpeed(self):
        return self._speed

    def attack(self, target):
        target.setHealth (target.getHealth() - self._power)

class Warrior(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        self.attack(target)

class Assasin(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self._power = 42
        self.speed = 7
        self.attack(target)

class Support(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._health = 500
        self._armor = 8
        self.speed = 4
    
    def special(self, target):
        self.speed = 6
        target.setHealth (target.getHealth() + 150)

warrior = Warrior("Mayko",10)
assassin = Assasin("Wira", 25)
support = Support("Radit", 30)

print("health (before) ", warrior.getHealth())
assassin.attack(warrior)
print("health (after) ", warrior.getHealth())

print("-"*10)

print("Warrior (health) ", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())

support.special(warrior)

print("Warrior (health) ", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())