class Hero: #template
    #class variabel
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)


hero1 = Hero("zilong",100, 10, 5)
print(Hero.jumlah)
hero2 = Hero("alucard",500, 20, 3)
print(Hero.jumlah)
hero3 = Hero("miya",1000, 50, 5)
print(Hero.jumlah)