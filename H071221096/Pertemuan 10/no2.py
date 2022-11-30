from abc import ABC, abstractmethod

class Attributes(ABC):
    @abstractmethod
    def role(self):
        pass

class Strength(Attributes):
    def __init__(self, heroes, skill):
        self.__heroes = heroes
        self.__skill = skill
    
    def role(self):
        print(f"{strength} pada umumnya memiliki role sebagai offlaner / soft support")

class Agility(Attributes):
    def __init__(self, heroes, skill):
        self.__heroes = heroes
        self.__skill = skill
    
    def role(self):
        print(f"{agility} pada umumnya memiliki role sebagai carry")

class Intelligence(Attributes):
    def __init__(self, heroes, skill):
        self.__heroes = heroes
        self.__skill = skill
    
    def role(self):
        print(f"{intelligence} pada umumnya memiliki role sebagai midlaner / hard support ")
    
class Magnus(Strength):
    def __init__(self, heroes, skill):
        super().__init__(heroes, skill)
        self._build = "Arcane Boots ==> Blink Dagger ==> Aghanim Shard"
        self._ultimate = "Reverse Polarity"
        self._user = "Collapse, ceb, Faith_bian"

    def role(self):
        print(f"Magnus pada umumnya memiliki role sebagai offlaner (initiator)")

    def build(self):
        print(f"build yang paling umum biasanya {self._build}")
    
    def ultimate(self):
        print(f"Magnus memiliki ultimate yang bernama {self._ultimate}")

    def user(self):
        print(f"Magnus dikenal karena dipakai oleh {self._user}")

def tes_role(strength):
    strength.role()

class Juggernaut(Agility):
    def __init__(self, heroes, skill):
        super().__init__(heroes, skill)
        self._build = "Diffusal Blade/Maelstrom ==> Yasha ke Manta Style ==> Butterfly/Abyssal Blade"
        self._ultimate = "Omnislash"
        self._user = "Yatoro, Miracle"

    def role(self):
        print(f"Juggernaut pada umumnya memiliki role sebagai carry (pusher/escape)")

    def build(self):
        print(f"build yang paling umum biasanya {self._build}")
    
    def ultimate(self):
        print(f"Juggernaut memiliki ultimate yang bernama {self._ultimate}")

    def user(self):
        print(f"Magnus dikenal karena dipakai oleh {self._user}")

def tes_role(agility):
    agility.role()

class Invoker(Intelligence):
    def __init__(self, heroes, skill):
        super().__init__(heroes, skill)
        self._build = "Hand of Midas ==> Orchid Malevolence ==> Aghanim Scepter"
        self._ultimate = "Invoke"
        self._user = "Topson, Miracle, bzm"

    def role(self):
        print(f"Invoker pada umumnya memiliki role sebagai midlaner (nuker/disabler/escape/pusher)")

    def build(self):
        print(f"build yang paling umum biasanya {self._build}")
    
    def ultimate(self):
        print(f"Invoker memiliki ultimate yang bernama {self._ultimate}")

    def user(self):
        print(f"Invoker dikenal karena dipakai oleh {self._user}")

def tes_role(intelligence):
    intelligence.role()

strength = "Spirit Breaker"
agility = "Phantom Lancer"
intelligence = "Pugna"
hero1 = Strength(strength, True)
hero2 = Magnus("Magnus", True)
hero3 = Agility(agility, True)
hero4 = Juggernaut("Juggernaut", True)
hero5 = Intelligence(intelligence, True)
hero6 = Invoker("Invoker", True)

print("=" * 80)

tes_role(hero1)
tes_role(hero2)
hero2.build()
hero2.ultimate()
hero2.user()

print("=" * 80)

tes_role(hero3)
tes_role(hero4)
hero4.build()
hero4.ultimate()
hero4.user()

print("=" * 80)

tes_role(hero5)
tes_role(hero6)
hero6.build()
hero6.ultimate()
hero6.user()       



        
