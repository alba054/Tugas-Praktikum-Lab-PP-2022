class person:
    def __init__(self,name : str,age : int,isMale : bool):
        self.name = name
        self.age = age
        self.isMale = isMale
        
    def setName(self,name : str):
        self.name = name
        
    def setAge(self,age : int):
        self.age = age
        
    def setGender(self,isMale : bool):
        self.isMale = isMale
        
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)
        
    def getgender(self):
        if self.isMale :print("Pria")
        else : print("Wanita")