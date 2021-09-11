# overloading
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


    def getDamageReduce(self):
        return self.hp + self.armor
    
    def skill(self,powerup=None,effect=None):

        if powerup != None and effect != None :
            self.damage += powerup
            self.hp -= effect
        
        elif powerup != None and effect == None :
            self.damage += powerup
        
        return "success skill has been used"
    
    



# object
hero2 = Hero('Chaos Knight',1000,22,"Figter",100)
hero2.skill(100)
print(hero2.__dict__)

# self adalah sebuah parameter untuk mendefinisikan kepunyaan / atribute diri sendiri
# parameter adalah value yang di transfer dari saat method itu digunakan dan saat ia
# memiliki action