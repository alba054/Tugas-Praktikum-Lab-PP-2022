class Job:
    def __init__(self):
        pass
    
    def skill(self):
        pass
    
class Archer:
    def __init__(self,name):
        self.name = name
        self._speed = 65
        self._armor = 10
        self._health = 75
        self._power = 50
        
    def skill(self):
        self._speed += 50
        
class Warrior:
    def __init__(self,name):
        self.name = name
        self._health = 100
        self._power = 75
        self._armor = 75
        self._speed = 50
        
    def skillRace(self):
        self._health += 50
        self._power += 50
        
class MagicArcher(Archer):
    def __init__(self,name):
        super().__init__(name)
        self._speed = 50
        self.__magic = 50
        
    def skill(self):
        self._speed += 50
        self.__magic += 25
        
class Sniper(Archer):
    def __init__(self,name):
        super().__init__(name)
        self._speed = 50
        self.__power = 100
        
    def skill(self):
        self._speed += 50
        self.__power += 25
        
class SwordMaster(Warrior):
    def __init__(self,name):
        super().__init__(name)
        self._speed = 75
        self.__power = 110
        
    def skill(self):
        self._speed += 50
        self.__power += 25
class Guardian(Warrior):
    def __init__(self,name):
        super().__init__(name)
        self._health = 150
        self.__armor = 110
        del self._armor
        
    def skill(self):
        self._health += 75
        self.__armor += 25
        
nito = Guardian("nito")
print(nito.__dict__)
nito.skill()
print(nito.__dict__)