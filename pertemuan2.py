# Class
class Hero:
    # method 
    def __init__(self,name,hp,armor,role,damage):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.role = role
        self.damage = damage
        
    def getTotalHp(self):
        return '{}'.format(self.hp * self.armor)
    
    def menyerang(self,lawan):
        print("{} menyerang {}".format(self.name,lawan.name))
        lawan.hp -= self.damage
        return "attribute {} sekarang adalah {}".format(lawan.name,lawan.__dict__)




# object
hero1 = Hero('Mirana',200,12,"Agility",400)
hero2 = Hero('Chaos Knight',1000,22,"Figter",100)
print(hero2.__dict__)
print(hero1.menyerang(hero2))

