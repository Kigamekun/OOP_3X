# enkapsulasi 
class Hero():
    def __init__(self,name,hp,armor,role,damage):
        self.__name = name
        self.__hp = hp
        self.__armor = armor
        self.__role = role
        self.__damage = damage   
        
    def getName(self):
        return self.__name
    
    def setName(self,newname):
        self.__name = newname


        
hero1 = Hero("Huskar",400,20,"Agi",500)
