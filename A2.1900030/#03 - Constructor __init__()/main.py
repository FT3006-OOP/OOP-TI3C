class Hero: #template
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero ("sniper", 100, 10, 5)
hero2 = Hero ("luna", 1000, 250, 500)
hero3 = Hero ("Ucup", 5000, 1000, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)