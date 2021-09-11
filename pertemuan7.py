# inheritance 

class Hero():
    def __init__(self,name,hp,armor,role,damage):
        self.__name = name
        self.__hp = hp
        self.__armor = armor
        self.__role = role
        self.__damage = damage  
        
    def info(self):
        return self.__dict__ 
        
        
# ini inheritance
class Mage(Hero):
    
    def getRole(self):
        return "ini adalah hero mage"
    
class Figter(Hero):
    
    def getRole(self):
        return "ini adalah hero figter"
    

        
hero1 = Mage("Lich",400,20,"Agi",500)       
hero2 = Figter("Lycan",400,20,"Agi",500)
print(hero1.getRole())
print(hero2.getRole())
