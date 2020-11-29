class Hero :

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self.lawan):
        print(self.name + 'kita serang' + lawan.name )
        lawan.kitadiserang(self, self.attackPower)

    def kitadiserang(self, lawan, attackPower_lawan)
        print(self.name + 'kita di serang' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str (attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + 'tersisa' + str(self.health))

chikal = Hero('chikal', 100, 10, 5)
januar = Hero('januar', 100, 5, 10)

chikal.serang(januar)
print("\n")
januar.serang(chikal)
print('\n')