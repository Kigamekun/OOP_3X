# polymorpishm

class Hero():    
    def __init__(self, name, health, attackPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        
    def attack(self):
        return self.name+' menyerang musuh'
        

class HeroAgi(Hero):
    def attack(self):
        return self.name+' menyerang dengan Magic musuh'
        
class HeroStrength(Hero):
    def attack(self):
        return self.name+' menyerang dengan Basic attack musuh'
        

miya = Hero('Miya', 100, 10)
rubick = HeroAgi('Rubick', 100, 10)
axe = HeroStrength('Axe', 100, 10)

print(miya.attack()) 
print(rubick.attack()) 
print(axe.attack())


