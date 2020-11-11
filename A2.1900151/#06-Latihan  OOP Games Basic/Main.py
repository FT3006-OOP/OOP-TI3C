class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serbu(self, lawan):
        print(self.name + " serbu " + lawan.name)
        lawan.diserbu(self, self.attackPower)

    def diserbu(self, lawan, attackPower_lawan):
        print(self.name + " diserbu " + lawan.name)
        sakit_diterima = attackPower_lawan/self.armorNumber
        print("sakit diterima : " + str(sakit_diterima))
        self.health -= sakit_diterima
        print( "nyawa saya : " + self.name + " tersisa " + str(self.health))

pocong = Hero("pocong",100,10,5)
kunti = Hero("kunti",100,20,10)

pocong.serbu(kunti)
print("\n")
kunti.serbu(pocong)
print("\n")