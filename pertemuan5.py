# init / constructor / construct

class Hero():
    def __init__(self,name,hp,armor,role,damage):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.role = role
        self.damage = damage     

        
hero1 = Hero("Huskar",400,20,"Agi",500)