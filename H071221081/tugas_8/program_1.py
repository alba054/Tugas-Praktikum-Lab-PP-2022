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
        return self.name
        
    def getAge(self):
        return self.age
        
    def getGender(self):
        if self.isMale : return "Pria"
        else : return "Wanita"
        
orang = person("nito", 18, False)
print(orang.getGender())