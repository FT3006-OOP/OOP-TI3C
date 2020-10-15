class Hero: #template
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama" + inputName)

hero1 = Hero ("sniper", 100, 10, 5)
print(Hero.jumlah)
hero2 = Hero ("luna", 1000, 250, 500)
print(Hero.jumlah)
hero3 = Hero ("Ucup", 5000, 1000, 0)
print(Hero.jumlah)
