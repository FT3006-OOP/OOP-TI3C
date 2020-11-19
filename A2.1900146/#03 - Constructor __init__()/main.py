class Hero: #template


    def __init__(self, inputName, ibputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

Hero1 = Hero("Sniper",100, 10, 4)
Hero2 = Hero("Mirana",100, 15, 1)
Hero3 = Hero("Ucup",1000, 100, 0)

print(Hero1.__dict__)
print(Hero2.__dict__)
print(Hero3.__dict__)