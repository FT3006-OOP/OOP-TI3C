class Hero: # template

    def __init__(self, inputName, inputHealth, inputPower)
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("zilong",100, 10, 5)
hero2 = Hero("alucard",500, 20, 3)
hero3 = Hero("miya",1000, 50, 5)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)